from labkey.api_wrapper import APIWrapper
import json
import os
from urllib.parse import urlparse


__DEFAULT_REPORT_CONFIG_FILE = 'report_config.json'
__USER_EMAIL_ENV = "LABKEY_EMAIL"       # note USER is common UNIX env, don't use
__APIKEY_ENV = "LABKEY_API_KEY"

__api_key = None
__email = None
__report_config = None
__api_wrapper = None


def __report_config_init(config_json=None, config_file=None):
    global __DEFAULT_REPORT_CONFIG_FILE, __USER_EMAIL_ENV, __APIKEY_ENV
    global __api_key, __email, __report_config

    if __report_config is not None:
        return
    __report_config = {"domain":None, "containerPath":None, "contextPath":None, "useSsl":None}

    if config_json is None:
        if config_file is None and os.path.isfile(__DEFAULT_REPORT_CONFIG_FILE):
            config_file = __DEFAULT_REPORT_CONFIG_FILE
        if config_file is not None:
            config_json = json.load(open(config_file))

    __report_config = __report_config | dict(config_json or {})
    if 'parameters' not in __report_config:
        __report_config['parameters'] = {}

    if os.getenv(__APIKEY_ENV):
        __api_key = os.getenv(__APIKEY_ENV)
    elif __report_config.get("apiKey"):
        __api_key = __report_config.get("apiKey")

    if os.getenv(__USER_EMAIL_ENV):
        __email = os.getenv(__USER_EMAIL_ENV)
    elif __report_config.get("email"):
        __email = __report_config.get("email")

    if __report_config.get('baseUrl'):
        url = urlparse(__report_config.get('baseUrl'))
    if __report_config.get('useSsl') is None:
        __report_config['useSsl'] = url.scheme != 'http'
    if __report_config.get('domain') is None:
        __report_config['domain'] = url.netloc
    if __report_config.get('contextPath') is None:
        __report_config['contextPath'] = url.path

    if __report_config['domain'] is None:
        raise Exception("Could not construct LabKey server URL: domain")
    if __report_config['containerPath'] is None:
        raise Exception("Could not construct LabKey server URL: containerPath")
    if __report_config['contextPath'] is None:
        raise Exception("Could not construct LabKey server URL: contextPath")
    if __report_config['useSsl'] is None:
        raise Exception("Could not construct LabKey server URL: useSSL")

    if __report_config['domain'] is None or __report_config['containerPath'] is None or __report_config['contextPath'] is None or __report_config['useSsl'] is None:
        raise Exception("Could not construct LabKey server URL")

    return


def get_report_api_wrapper():
    global __api_wrapper, __report_config
    if __api_wrapper is None:
        __report_config_init()
        __api_wrapper = APIWrapper(__report_config['domain'], __report_config['containerPath'], __report_config['contextPath'], __report_config['useSsl'], api_key=__api_key)
    return __api_wrapper


def get_report_parameters():
    return dict(__report_config['parameters'])


def get_report_data():
    global __report_config

    __report_config_init()
    if not 'sourceQuery' in __report_config:
        return None

    q = __report_config['sourceQuery']
    columns = None
    if 'columns' in q:
        columns = ",".join(q['columns'])
    sort = ""
    if 'sort' in q:
        sort = q['sort']
    query_filters = []
    if 'filterArray' in q:
        array = q['filterArray']
        for i in range(0,len(array)):
            f = array[i]
            query_filters.add(QueryFilter(f[0],f[1],f[2]))
    parameters = {}
    if 'parameters' in q:
        parameters = q['parameters']
    container_filter = None
    if 'containerFilter' in q:
        container_filter = q['containerFilter']
    required_version=17.1
    if 'requiredVersion' in q:
        required_version = q['requiredVersion']

    # Not caching this, because it can be large
    return get_report_api_wrapper().query.select_rows(q['schemaName'], q['queryName'],
            container_filter=container_filter,
            max_rows=-1,
            offset=0,
            columns=columns,
            sort=sort,
            filter_array=query_filters,
            parameters=parameters,
            required_version=required_version
            )


    def dumps(self):
        j = dict(self.config)
        j['apiKey'] = __api_key 
        j['email'] = __email
        return str(j)


# TEST
#
if __name__ == '__main__':
    __report_config_init(config_json={
        "baseUrl" : "http://localhost:8080/labkey/",
        "containerPath" : "/home",
        # "apiKey" : "{{APIKEY}}",        # optionally passed in via environment
        # "email" : "user1@test.com",     # optionally passed in via environment
        "parameters" : { 'xmin':0, 'xmax':100, 'type':"sample" },
        "sourceQuery": {
            #"columns":[["X"],["ModifiedBy", "DisplayName"]],   # python library doesn't deal with field keys
            "columns" : ["X", "ModifiedBy/DisplayName"],
            "requiredVersion":17.1,
            "queryName":"asdf",
            "schemaName":"lists"
        }
    })
    data = get_report_data()
    print(json.dumps(data))
