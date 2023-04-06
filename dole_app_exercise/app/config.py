import os


class Config(object):
    """
    Common configurations
    """
    SECRET_KEY = os.urandom(16)
    ASSETS_DEBUG = True
    CSRF_ENABLED = True
    directory_path = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(directory_path, 'dole_db.db')


class DevelopmentConfig(Config):
    """
    Configurations for development
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    Configurations for production
    """
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
