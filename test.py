from flask import Flask
from flask_restplus import Api, Resource, fields, abort
# from main.constants import *
from utils.utils import *
from models.models import *
import traceback

app = Flask(__name__)
api = Api(app)

ns = api.namespace("login", description="Login Operation")


login_parser = api.parser()
login_parser.add_argument("username", required=True)
login_parser.add_argument("password", required=True)

logout_parser = api.parser()
logout_parser.add_argument("username", required=True)

@ns.route("/")
@api.doc(responses={500: "Resource Not Found"})
class Login(Resource):

    @api.doc(parser=login_parser)
    def post(self):
        try:
            args = login_parser.parse_args()
            username = args["username"]
            password = args["password"]
            if username=='talha' and password=='myoass':
                ross = auth_manager(user_id=username)
                ross.session_id = 'some_session_id'
                ross.password = password
                ross.save()
                return "Successfully logged in", 201
            else:
                abort("Invalid credentials",404)

        except:
            return "Some error occured", 404


    @api.doc(responses={500: "Resource Not Found"})
    class Logout(Resource):

        @api.doc(parser=logout_parser)
        def post(self):
            try:
                return "Successfully logout", 201

            except:
                return "Failure database", 404

if __name__ == "__main__":
    app.run(debug=True)
