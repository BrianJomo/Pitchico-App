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
     SQLALCHEMY_DATABASE_URI = 'postgresql://sorzwxhfwblzaa:2c926243af97319b412f4cb7cfb4943d0bcfa9bce456f339737bf0aa8d175dff@ec2-54-86-224-85.compute-1.amazonaws.com:5432/dfk5dgeselavkp'
    
     pass



class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}