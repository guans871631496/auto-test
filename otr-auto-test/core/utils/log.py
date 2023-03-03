import logging
from config.project_path import *
import time


class LoggerHandler(logging.Logger):
    def __init__(self,
                 name='root',
                 logger_level='DEBUG',
                 file=None,
                 logger_format=" [%(asctime)s]  %(levelname)s %(filename)s [ line:%(lineno)d ] %(message)s"
                 ):

        super().__init__(name)
        self.setLevel(logger_level)
        handler_format = logging.Formatter(logger_format)

        if file:
            file_handler = logging.FileHandler(file)
            file_handler.setLevel(logger_level)
            file_handler.setFormatter(handler_format)
            self.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logger_level)
        stream_handler.setFormatter(handler_format)
        self.addHandler(stream_handler)


logger = LoggerHandler()
