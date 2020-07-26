#!ServiceHelper/bin/python
import sys
import json
from code_files.configuration import Config
from code_files.logger import Logger


class ServiceHelper():
    def __init__(self, config_file_path):
        main_config = Config(config_file_path)
        self.config = main_config.get_config()
        self.logger = Logger(main_config)
        self.logger.set_logger()
        self.state= self.load_config()

    def load_config(self):
        try:
            with open(self.config["state_file"],encoding="utf-8") as json_data_file:
                return json.load(json_data_file)
        except IOError as e:
            print("IO error:", sys.exc_info()[0])
        except:
            print("Unexpected error:", sys.exc_info()[0])

    def set(self,state):
        try:
            with open(self.config["state_file"],mode="w", encoding="utf-8") as json_data_file:
                json.dump(state,json_data_file,ensure_ascii=False)
            self.logger.logger.info(self.state)

        except Exception as e:
            self.logger.logger.error(e)

    def get(self):
        try:
            return self.state

        except Exception as e:
            self.logger.logger.error(e)




