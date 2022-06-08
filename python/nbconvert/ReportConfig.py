from labkey.api_wrapper import APIWrapper
import json
import os
from urllib.parse import urlparse


DEFAULT_REPORT_CONFIG_FILE = 'report_config.json'
USER_EMAIL_ENV = "LABKEY_EMAIL"       # note USER is common UNIX env, don't use
APIKEY_ENV = "LABKEY_API_KEY"    


#
# example config object
#
# NOTE: The config file json is not meant to be language specific, it uses our typical
# camelCase naming convention.

config_example = { 
        "baseUrl" : "http://localhost:8080/labkey/",
        "containerPath" : "/home", 
        "apiKey" : "{{APIKEY}}",        # optionally passed in via environment
        "email" : "user1@test.com",     # optionally passed in via environment
        "parameters" : { 'xmin':0, 'xmax':100, 'type':"sample" },
        "sourceQuery": {
            "columns":[["X"],["ModifiedBy", "DisplayName"]], 
            "requiredVersion":17.1, 
            "queryName":"asdf", 
            "schemaName":"lists"
        }
    }
#


class ReportConfig:

    # the config parameters are mostly for testing/dev, runtime will use default report_config.json
    # Don't provide both a config object and config_file (config object will take precedence)

    def __init__(self, config=None, config_file=None):
        self.api_key = None
        self.email = None
        self.api = None
        self.config = {}
       
        if config is None:
            if config_file is None and os.path.isfile(DEFAULT_REPORT_CONFIG_FILE):
                config_file = DEFAULT_REPORT_CONFIG_FILE
            if config_file is not None:
                config = json.load(open(config_file))

        self.config = dict(config or {})
        if 'parameters' not in self.config:
            self.config['parameters'] = {}
 
        if os.getenv(APIKEY_ENV):
            self.api_key = os.getenv(APIKEY_ENV)
        if self.config.get("apiKey"):
            self.api_key = self.config.get("apiKey")
        
        if os.getenv(USER_EMAIL_ENV):
            self.email = os.getenv(USER_EMAIL_ENV)
        if self.config.get("email"):
            self.email = self.config.get("email")

        if self.config.get('baseUrl'):
            url = urlparse(self.config.get('baseUrl'))
            if self.config.get('useSsl') is None:
                self.config['useSsl'] = url.scheme != 'http'
            if self.config.get('domain') is None:
                self.config['domain'] = url.netloc
            if self.config.get('contextPath') is None:
                self.config['contextPath'] = url.path

        if not self.config['domain'] or self.config['containerPath'] is None or self.config['contextPath'] is None or self.config['useSsl'] is None:
            raise Exception("Could not construct LabKey server URL")

        self.api = APIWrapper(self.config['domain'], self.config['containerPath'], self.config['contextPath'], self.config['useSsl'],
                api_key=self.api_key)
        return


    def get_source_data(self):
        if not 'sourceQuery' in self.config:
            return None
        q = self.config['sourceQuery']
        columns = "*"
        if 'columns' in q:
            columns = q['columns']
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
        containerFilter = None
        if 'containerFilter' in q:
            containerFilter = q['containerFilter']

        api = self.get_api_wrapper()
        return api.query.select_rows(q['schemaName'], q['queryName'],
                #containerFilter=containerFilter,
                max_rows=-1,
                offset=0,
                columns=columns,
                sort=sort,
                filter_array=query_filters,
                parameters=parameters,
                required_version=q['requiredVersion']
                )


    def __str__(self):
        j = dict(self.config)
        j['apiKey'] = self.api_key 
        j['email'] = self.email
        return str(j)


    def get_api_wrapper(self):
        return self.api

    
    def get_data():
        return


#
report = ReportConfig(config=config_example)
data = report.get_source_data()
print(data)
