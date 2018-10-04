class Config(object):

    DEBUG = False
    TESTING = False
    SECRET_KEY = 'rubarema'


class DevelopmentConfig(Config):

    DEBUG = True
    TESTING = False
    ENV = "development"
    SECRET_KEY = 'rubarema'
