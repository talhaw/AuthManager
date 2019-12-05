from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'talhayounus1996@gmail.com'
app.config['MAIL_USERNAME'] = 'talhayounus1996@gmail.com'
app.config['MAIL_PASSWORD'] = 'Messi+Suarez==109'
app.config.from_pyfile('config.py')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@0.0.0.0:3306/apnaschoolmysqldb'
mail = Mail(app)

db = SQLAlchemy(app)


if __name__ == "__main__":
    from auth.api import *
    app.run(host="0.0.0.0", debug=False)
