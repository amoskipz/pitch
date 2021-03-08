import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    # SQLALCHEMY_DATABASE_URI="postgres://moringa:Access@localhost:5432/amos"
    print (SQLALCHEMY_DATABASE_URI, "00000")
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 2435
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'pitch'
    SENDER_EMAIL = 'koechkipz03@gmail.com'
    SECRET_KEY = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
    
# simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # SECRET_KEY="amos3378"
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch_test'
    # SECRET_KEY="amos3378"
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI="postgres://moringa:Access@localhost:5432/amos"
    DEVELOPMENT = True
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}
