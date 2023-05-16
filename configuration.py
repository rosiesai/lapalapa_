class Config(object):
    """Base config, uses staging database server."""
    SECRET_KEY = "BaseKey"
    DEBUG = True
    TESTING = False
    #DB_SERVER = '192.168.1.56'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root123@localhost:3306/ejemplo"


class ProductionConfig(Config):
    """Uses production database server."""
    #DB_SERVER = '192.168.19.32'
    DEBUG = False

class DevelopmentConfig(Config):
    SECRET_KEY = "DesarrolloKey"
    DEBUG = True
    TESTING = True
   # DB_SERVER = 'localhost'

