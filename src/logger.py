import logging
from logging.handlers import RotatingFileHandler
import os
import json

class Logger:
    _instance = None
    _config = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, name):
        if not hasattr(self, 'logger'):
            self.load_config()
            self.logger = logging.getLogger(name)
            self.logger.setLevel(self._config['level'])
            self.handler = RotatingFileHandler(self._config['file'], maxBytes=self._config['max_bytes'], backupCount=self._config['backup_count'])
            self.handler.setLevel(self._config['level'])
            self.formatter = logging.Formatter(self._config['format'])
            self.handler.setFormatter(self.formatter)
            self.logger.addHandler(self.handler)
            self.stream_handler = logging.StreamHandler()
            self.stream_handler.setLevel(self._config['level'])
            self.stream_handler.setFormatter(self.formatter)
            self.logger.addHandler(self.stream_handler)
            self.error_handler = logging.FileHandler(self._config['error_file'])
            self.error_handler.setLevel(logging.ERROR)
            self.error_formatter = logging.Formatter(self._config['error_format'])
            self.error_handler.setFormatter(self.error_formatter)
            self.logger.addHandler(self.error_handler)

    def load_config(self):
        try:
            with open('logging_config.json', 'r') as f:
                self._config = json.load(f)
        except FileNotFoundError:
            self._config = {
                'level': 'DEBUG',
                'file': 'app.log',
                'max_bytes': 1000000,
                'backup_count': 1,
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                'error_file': 'error.log',
                'error_format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            }

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
