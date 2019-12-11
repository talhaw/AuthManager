from celery import Celery
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

mail = Mail(app)

db = SQLAlchemy(app)

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], backend=app.config['CELERY_RESULT_BACKEND'],include='auth.api')
celery.conf.update(app.config)

if __name__ == "__main__":
    from auth.api import *
    app.run(host="0.0.0.0", debug=True)
