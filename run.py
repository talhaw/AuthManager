from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')

if __name__ == "__main__":
    from auth.api import *
    app.run(debug=True)
