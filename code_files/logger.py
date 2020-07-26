import logging
import time
import os


class Logger:
    def __init__(self,configuration):
        self.log_dir_path= configuration.get_log_dir_path()
        self.log_level=configuration.get_log_level()
        self.logger = logging.getLogger(configuration.get_log_name())

    def set_logger(self):
        try:
            self.logger.setLevel(self.log_level)
            # create console handler and set level to debug
            ch = logging.StreamHandler()
            ch.setLevel(self.log_level)
            # create file handler and set level to info
            file_name = time.strftime("%Y-%m-%d") + '.log'
            file_path = self.log_dir_path
            file_location = os.path.join(file_path,file_name)

            fl = logging.FileHandler(filename=file_location, encoding='utf-8')
            fl.setLevel(self.log_level)

            # create formatter
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            # add formatter to ch
            ch.setFormatter(formatter)
            # add formatter to ch
            fl.setFormatter(formatter)

            # add handlers to logger
            self.logger.addHandler(ch)
            self.logger.addHandler(fl)
        except:
            print("Unable to create Logger")