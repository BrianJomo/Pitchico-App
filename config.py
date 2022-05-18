import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Romanoz@localhost/pitchico'
    SECRET_KEY = os.urandom(32)
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitchico'
    SENDER_EMAIL = 'testrandy78@gmail.com'

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
     SQLALCHEMY_DATABASE_URI =os.environ.get("SQLALCHEMY_DATABASE_URI")
    
     pass



class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}