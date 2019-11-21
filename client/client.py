import traceback
import hashlib
import uuid

from models.models import *



class MongoClient(object):
    def __init__(self, db_name, host, port):
        self.conn = connect(db_name, host=host, port=port)

    def return_connection(self):
        return self.conn

    def add_session(self, username, password, role):
        try:
            auth = AuthManager(user_id=username)
            auth.session_id = str(uuid.uuid1())
            auth.role = role
            auth.save()
            return 200, auth.session_id

        except BaseException:
            return 500

    def delete_session(self, session_id):
        try:
            if AuthManager.objects(session_id=session_id):
                AuthManager.objects(session_id=session_id).delete()
                return 204, session_id

            else:
                return 403, ""

        except BaseException:
            return 500

    def get_session(self, session_id):
        try:
            if AuthManager.objects(session_id=str(session_id)):
                user = AuthManager.objects(session_id=session_id).get()
                return 201, user
            else:
                return 404, "Not logged in"

        except BaseException:
            return 500, "Internal server error"
