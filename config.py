from run import app

DEBUG = False
port = '3307'
db_name = 'apnaschoolmysqldb'
host = 'db'
SECRET_KEY = "ThisisaSecret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@0.0.0.0:3307/{}'.format(db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
