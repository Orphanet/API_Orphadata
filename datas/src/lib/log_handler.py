import logging
import logging.config

from . import utils
utils.addLoggingLevel('BASIC_LOG', 55, methodName='basic_log')

class Logger:
    def __init__(self, name, outpath=None):
        if outpath:
            config = get_config(outpath=outpath)
            logging.config.dictConfig(config)

        self.logger = logging.getLogger(name)

    @staticmethod
    def deco(log):
        return '-' * len(log)

    def title(self, log):
        self.logger.info('')
        self.logger.info('')
        deco = self.deco(log)
        self.logger.info(log.upper())
        self.logger.info(deco)

    def debug(self, log):
        self.logger.debug(log)

    def info(self, log):
        self.logger.info(log)

    def warning(self, log):
        self.logger.warning(log)

    def error(self, log):
        self.logger.error(log)

    def critical(self, log):
        self.logger.critical(log)

    def basic_log(self, log):
        self.logger.basic_log(log)


def get_logger(name, outpath=None):
    if outpath:
        config = get_config(outpath=outpath)
        logging.config.dictConfig(config)

    return logging.getLogger(name)


def get_config(outpath='./'):
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "detailed": {
                "format": "%(asctime)-12s %(name)-28s %(levelname)-10s %(message)s",
                "datefmt": "%D at %H:%M:%S"
            },
            "simple": {
                "format": "%(message)s"
            }
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "BASIC_LOG",
                "formatter": "detailed"
            },

            "info_handler": {
                "class": "logging.FileHandler",
                "level": "NOTSET",
                "formatter": "detailed",
                "filename": outpath,
                "mode": "w+",
                "encoding": "utf8",
                "delay": False
            }
        },

        "root": {
            "level": "NOTSET",
            "handlers": ["console", "info_handler"],
            "propagate": False
        }
    }

    return config