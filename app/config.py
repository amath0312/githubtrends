import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class BaseConfig:
    SECRET_KEY = 'aaaaa'
    PKYX_MAIL_SENDER = 'PK一下 amath321@163.com'
    PKYX_MAIL_SUBJECT_PREFIX = '[PKYX]'
    
    @staticmethod
    def init_app(app):
        pass
        
        
class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
    print(SQLALCHEMY_DATABASE_URI)
    @staticmethod
    def init_app(app):
        return app
        
config = {
    'dev': DevConfig
}