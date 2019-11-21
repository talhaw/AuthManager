import sqlalchemy
from flask import request

from .utils import *
from init import db


@app.before_first_request
def setup():
    engine = sqlalchemy.create_engine('mysql://root:''@db:3306/apnaschoolmysqldb')
    User.metadata.drop_all(engine)


@app.route('/login', methods=['POST'])
def login():
    try:
        print('Loginnnnn')
        result = request.form
        username = result["username"]
        print('In login route')

        password = result["password"]
        role = result["role"]
        password = hashlib.sha1(password.encode()).hexdigest()
        status, session_id = service_layer.add_session(
            username=username, password=password, role=role
        )

        if status == 200:
            response_body = {
                "message": "Successfully logged in",
                "session_id": session_id,
            }
            return response_body, 200

        elif status == 500:
            response_body = {"message": "Internal server error"}
            return response_body, 500

    except BaseException:
        response_body = {"message": "Internal server error"}
        return response_body, 500


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    try:
        result = request.form
        session_id = result["session_id"]
        print('In logout route')
        status, s_id = service_layer.delete_session(
            session_id=str(session_id))

        if status == 204:
            response_body = {
                "message": "Successfully logged out",
                "session_id": s_id,
            }
            return response_body, 204

        elif status == 403:
            response_body = {"message": "This user is not logged in"}
            return response_body, 403

        elif status == 500:
            response_body = {"message": "Internal server error"}
            return response_body, 500

    except BaseException:
        response_body = {"message": "Internal server error"}
        return response_body, 500


@app.route('/validate', methods=['POST', 'GET'])
def validate():
    try:
        result = request.form
        session_id = result["session_id"]
        print('In validate route')
        status, role = service_layer.get_session(session_id=session_id)
        if status == 201:
            response_body = {
                "message": "Successfully get role",
                "session_id": session_id,
                "role": role,
            }
            return response_body, 409

        elif status == 404:
            response_body = {
                "message": "Not found",
                "session_id": session_id}
            return response_body, 404

        elif status == 500:
            response_body = {"message": "Internal server error"}
            return response_body, 500

    except BaseException:
        response_body = {"message": "Internal server error"}
        return response_body, 500


@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        db.create_all()
        result = request.form

        name = result["name"]
        age = result["age"]
        grade = result["grade"]
        department = result["department"]
        password = result["password"]
        print('\nUser info = ',name, age, grade, department, password)
        new_user = User(name, age, grade, department, password)
        with app.app_context():

            db.session.add(new_user)
            db.session.commit()
            db.session.close()
        response_body = {"message": "User added successfully"}
        return response_body, 200

    except BaseException:
        response_body = {"message": "Error occured while adding user"}
        return response_body, 404


@app.route('/delete_user', methods=['POST', 'GET'])
def delete_user():
    # db.create_all()

    result = request.form
    # name = result["name"]

    user_id = result["user_id"]
    quer = db.session.query(User).filter(User.user_id == user_id).delete()
    db.session.commit()
    db.session.close()
    if quer:
        response_body = {"message": "User deleted successfully"}
        return response_body, 200

    else:
        response_body = {"message": "User with this id not found "}
        return response_body, 404

    # except BaseException:
    #     response_body = {"message": "Internal Server error"}
    #     return response_body, 500


@app.route('/get_user', methods=['POST', 'GET'])
def get_user():
    db.create_all()

    result = request.form
    # name = result["name"]

    user_id = result["user_id"]
    quer = db.session.query(User).filter_by(User.user_id == user_id)
    db.session.commit()
    db.session.close()
    if quer:
        response_body = {"message": "User exists with this id"}
        return response_body, 200

    else:
        response_body = {"message": "User with this id not found "}
        return response_body, 404

    # except BaseException:
    #     response_body = {"message": "Internal Server error"}
    #     return response_body, 500
