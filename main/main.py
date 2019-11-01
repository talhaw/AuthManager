from flask import Flask
from flask_restplus import Api, Resource, fields, abort
from service.service import *
from db.client import *
import json

app = Flask(__name__)
api = Api(app)

ns = api.namespace("login", description="Login Operation")
log_off = api.namespace("logout", description="Logout Operation")
validate = api.namespace("validate", description="Validation Operation")

login_parser = api.parser()
login_parser.add_argument("username", required=True)
login_parser.add_argument("password", required=True)
login_parser.add_argument("role", required=True)

logout_parser = api.parser()
logout_parser.add_argument("session_id", required=True)

validate_parser = api.parser()
validate_parser.add_argument("session_id", required=True)

cli = MongoClient(db_name="auth_model", host="0.0.0.0", port=27017)
service_layer = ServiceLayer(cli)

@ns.route("/")
@api.doc(responses={500: "Resource Not Found"})
class Login(Resource):
    @api.doc(parser=login_parser)
    def post(self):
        try:
            args = login_parser.parse_args()
            username = args["username"]
            password = args["password"]
            role = args["role"]
            password = hashlib.sha1(password.encode()).hexdigest()
            status, session_id = service_layer.add_session(
                username=username, password=password, role=role
            )

            if status == 200:
                response_body = {
                    'message': 'Successfully logged in',
                    'session_id': session_id
                }
                return response_body, 200

            elif status == 500:
                response_body = {
                    'message': 'Internal server error'
                }
                return response_body, 500

        except:
            response_body = {
                'message': 'Internal server error'
            }
            return response_body, 500

    @log_off.route("/")
    @api.doc(responses={500: "Resource Not Found"})
    class Logout(Resource):
        @api.doc(parser=logout_parser)
        def post(self):
            try:
                args = logout_parser.parse_args()
                session_id = args["session_id"]
                status, s_id = service_layer.delete_session(session_id=str(session_id))

                if status == 204:
                    response_body = {
                        'message': 'Successfully logged out',
                        'session_id': s_id
                    }
                    return response_body, 204

                elif status == 403:
                    response_body = {
                        'message': 'This user is not logged in'
                    }
                    return response_body, 403

                elif status == 500:
                    response_body = {
                        'message': 'Internal server error'
                    }
                    return response_body, 500

            except:
                response_body = {
                    'message': 'Internal server error'
                }
                return response_body, 500

    @validate.route("/")
    @api.doc(responses={500: "Resource Not Found"})
    class Validate(Resource):
        @api.doc(parser=validate_parser)
        def get(self):
            try:
                args = validate_parser.parse_args()
                session_id = args["session_id"]
                status, role = service_layer.get_session(session_id=session_id)
                if status == 201:
                    response_body = {
                        'message': 'Successfully get role',
                        'session_id': session_id,
                        'role': role
                    }
                    return response_body, 409

                elif status == 404:
                    response_body = {
                        'message': 'Not found',
                        'session_id': session_id
                    }
                    return response_body, 404

                elif status == 500:
                    response_body = {
                        'message': 'Internal server error'
                    }
                    return response_body, 500

            except:
                response_body = {
                    'message': 'Internal server error'
                }
                return response_body, 500


if __name__ == "__main__":
    app.run(debug=True)
