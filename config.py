#null
class Config:
    DEBUG=True
    TESTING=True

    #CONFIGURACION BASE DATOS 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:ronald12345@localhost:3306/blog_db"

class ProductionsConfig(Config):
    DEBUG= False

class DevelopmentConfig(Config):
    SECRET_KEY='dev'
    DEBUG=True
