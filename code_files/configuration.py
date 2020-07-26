import json,sys,logging


class Config:
    def __init__(self, config_file_path):
        self.file_path = config_file_path
        self.config = {}
        self.load_config()

    def load_config(self):
        try:
            with open(self.file_path) as json_data_file:
                self.config = json.load(json_data_file)

        except IOError as e:
            print("IO error:", sys.exc_info()[0])

        except:
            print("Unexpected error:", sys.exc_info()[0])


    def get_log_dir_path(self):
        return self.config["logger"]["log_dir_path"]

    def get_log_name(self):
        return self.config["logger"]["log_name"]

    def get_spark_config(self):
        return self.config["spark_config"]

    def get_bi_sql_config(self):
        return self.config["sql_bridge_config"]

    def remove_metadata_from_config(self,dict_config,metadata_key):
        try:
            del dict_config[metadata_key]
        except Exception as e:
            print("configuration error:{}", sys.exc_info()[0])
        finally:
            return dict_config



    def get_log_level(self):
        level = logging.DEBUG
        if self.config["logger"]["log_level"] == "ERROR":
            level = logging.ERROR
        else:
            if self.config["logger"]["log_level"] == "INFO":
                level = logging.INFO
            else:
                if self.config["logger"]["log_level"] == "WARNING":
                    level = logging.WARNING
        return level

    def get_spark_log_level(self):
        level = logging.DEBUG
        if self.config["logger"]["log_level_spark"] == "ERROR":
            level = logging.ERROR
        else:
            if self.config["logger"]["log_level_spark"] == "INFO":
                level = logging.INFO
            else:
                if self.config["logger"]["log_level_spark"] == "WARNING":
                    level = logging.WARNING
        return level

    def get_config(self):
        return self.config


