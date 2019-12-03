from run import app

DEBUG = False
port = '3306'
db_name = 'apnaschoolmysqldb'
host = 'db'
SECRET_KEY = "ThisisaSecret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@0.0.0.0:3306/{}'.format(db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
