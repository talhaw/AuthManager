from celery import Celery
from auth_celery import make_celery
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'talhayounus1996@gmail.com'
app.config['MAIL_USERNAME'] = 'talhayounus1996@gmail.com'
app.config['MAIL_PASSWORD'] = 'Messi+Suarez==109'

app.config.from_pyfile('config.py')

mail = Mail(app)

db = SQLAlchemy(app)

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], backend=app.config['CELERY_RESULT_BACKEND'],include='auth.api')


celery.conf.update(app.config)

if __name__ == "__main__":
    from auth.api import *
    app.run(host="0.0.0.0", debug=True)
