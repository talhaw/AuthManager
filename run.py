import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy


app = Flask(__name__)

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

if __name__ == "__main__":
    from auth.api import *
    app.run(host="0.0.0.0", debug=False)
