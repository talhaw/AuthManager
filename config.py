from run import app

DEBUG = False
port = '3306'
db_name = 'apnaschoolmysqldb'
host = 'db'
SECRET_KEY = "ThisisaSecret"


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@0.0.0.0:3306/{}'.format(db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'talhayounus1996@gmail.com'
app.config['MAIL_USERNAME'] = 'talhayounus1996@gmail.com'
app.config['MAIL_PASSWORD'] = 'Messi+Suarez==109'