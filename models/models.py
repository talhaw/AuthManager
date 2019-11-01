from mongoengine import *

connect(
    'auth_model',
    host='0.0.0.0',
    port=27017
    )

class auth_manager(Document):
    user_id = StringField()
    session_id = StringField()
    password = StringField()
    # role = StringField(choices=["student", "teacher"])
    