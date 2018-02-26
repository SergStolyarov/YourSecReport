import os


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)
    MONGODB_HOST = '212.109.192.124'
    MONGODB_DBNAME = 'test_db'
    MONGODB_USERNAME = 'admin'
    MONGODB_PASSWORD = 'yoursecreport'
    

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True