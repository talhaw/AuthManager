from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@0.0.0.0:3306/apnaschoolmysqldb'

db = SQLAlchemy(app)

if __name__ == "__main__":
    from auth.api import *
    app.run(host="0.0.0.0", debug=False)
