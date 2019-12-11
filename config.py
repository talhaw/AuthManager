SECRET_KEY = "ThisisaSecret"

"""database configs """
DEBUG = False
port = '3306'
db_name = 'apnaschoolmysqldb'
host = 'db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

"""celery configs"""
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

"""mail config"""
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_DEFAULT_SENDER = 'talhayounus1996@gmail.com'
MAIL_USERNAME = 'talhayounus1996@gmail.com'
MAIL_PASSWORD = 'Messi+Suarez==109'
SQLALCHEMY_DATABASE_URI = 'mysql://root:''@db:3306/apnaschoolmysqldb'
