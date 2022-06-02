from labkey.api_wrapper import APIWrapper
import json
import os
from urllib.parse import urlparse


DEFAULT_REPORT_CONFIG_FILE = 'report_config.json'
USER_ENV = "LABKEY_EMAIL"       # note USER is common UNIX env, don't use
APIKEY_ENV = "LABKEY_API_KEY"    


#
# example config object
#
# NOTE: The config file json is not meant to be language specific, it uses our typical
# camelCase naming convention.

config_example = { 
        'baseUrl' : "http://localhost:8080/labkey/",
        'containerPath' : "/home", 
        'apiKey' : "{{APIKEY}}",
        'user' : "user1@test.com",
        'parameters' : { 'xmin':0, 'xmax':100, 'type':"sample" }
        }
#


class ReportConfig:

    # the config parameters are mostly for testing/dev, runtime will use default report_config.json
    # Don't provide both a config object and config_file (config object will take precedence)

    def __init__(self, config=None, config_file=None):
        self.api_key = None
        self.user = None
        self.api = None
        self.json = {}
       
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
        
        if os.getenv(USER_ENV):
            self.user = os.getenv(USER_ENV)
        if self.config.get("user"):
            self.user = self.config.get("user")

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

        self.api = APIWrapper(self.config['domain'], self.config['containerPath'], self.config['contextPath'], self.config['useSsl'])
        return


    def __str__(self):
        j = dict(self.config)
        j['apiKey'] = self.api_key 
        j['user'] = self.user
        return str(j)


    def get_api_wrapper(self):
        return self.api

    
    def get_data():
        return


