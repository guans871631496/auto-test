import logging
from loguru import logger
from config.project_path import *
import time


class Handler(logging.Handler):
    def emit(self, record):
        logging.getLogger(record.name).handle(record)


logger.add(Handler(), format="{time:YYYY-MM-DD at HH:mm:ss} | {message}")
logger.add(log_path+"/log_"+time.strftime('%Y-%m-%d_%H-%M-%S')+".log")
