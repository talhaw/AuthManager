from mongoengine import *


class AuthManager(Document):
    user_id = StringField()
    session_id = StringField()
    role = StringField(choices=["student", "teacher"])
