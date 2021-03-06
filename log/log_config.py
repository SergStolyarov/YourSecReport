import logging
import os
from functools import wraps
from logging.handlers import TimedRotatingFileHandler


def configlogging():
    package_dir = os.path.abspath(os.path.dirname(__file__))
    fmt = '%(asctime)s %(levelname)s %(message)s'
    filename = os.path.join(package_dir, 'app.log')
    formatter = logging.Formatter(fmt)
    handler = TimedRotatingFileHandler(filename, when="midnight", interval=1)
    handler.suffix = '%Y-%m-%d'
    handler.setFormatter(formatter)
    logger = logging.getLogger('app.server')
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


def log(logger):
    def decorator(func):
        @wraps(func)
        def call(*args, **kwargs):
            logger.info('%s %s: Function called', func.__module__, func.__name__)
            try:
                return func(*args, **kwargs)
            except:
                logger.exception('%s %s: Exception:', func.__module__, func.__name__)
                raise

        return call
    return decorator
