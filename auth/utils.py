from flask import Flask

from flask_restplus import Api

from client.client import *
from .views import *

app = Flask(__name__)
api = Api(app)

ns = api.namespace("login", description="Login Operation")
log_off = api.namespace("logout", description="Logout Operation")
validate = api.namespace("validate", description="Validation Operation")
add_user = api.namespace("user_add", description="User Add Operation")
delete_user = api.namespace("user_delete", description="User Delete Operation")

login_parser = api.parser()
login_parser.add_argument("username", required=True)
login_parser.add_argument("password", required=True)
login_parser.add_argument("role", required=True)

logout_parser = api.parser()
logout_parser.add_argument("session_id", required=True)

validate_parser = api.parser()
validate_parser.add_argument("session_id", required=True)

user_add_parser = api.parser()
user_add_parser.add_argument("name", required=True)
user_add_parser.add_argument("age", required=True)
user_add_parser.add_argument("grade", required=True)
user_add_parser.add_argument("department", required=True)
user_add_parser.add_argument("password", required=True)

user_delete_parser = api.parser()
user_delete_parser.add_argument("user_id", required=True)


cli = MongoClient(db_name="authmanager_db_1", host="0.0.0.0", port=27017)
service_layer = ServiceLayer(cli)
