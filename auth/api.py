import uuid
import hashlib
import sqlalchemy

from flask import Flask, request
from flask_restplus import Api

from run import db
from models.models import User, AuthManager

app = Flask(__name__)
api = Api(app)


# @app.before_first_request
# def setup():
#     engine = sqlalchemy.create_engine('mysql://root:''@0.0.0.0:3306/apnaschoolmysqldb')
#     User.metadata.drop_all(engine)
#     db.create_all()


@app.route('/login', methods=['POST'])
def login():
    print('Loginnnnn')
    result = request.form
    username = result["username"]
    print('In login route')

    password = result["password"]
    role = result["role"]
    password = hashlib.sha1(password.encode()).hexdigest()

    new_user = AuthManager(uuid, role, username)


    with app.app_context():

        db.session.add(new_user)
        db.session.commit()
        db.session.close()

    response_body = {
        "message": "Successfully logged in",
        "session_id": 'session_id',
    }
    return response_body, 200


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    result = request.form
    session_id = result["session_id"]

    quer = db.session.query(AuthManager).filter(AuthManager.session_id == session_id).delete()
    db.session.commit()
    db.session.close()

    if quer:
        response_body = {"message": "User logged out successfully"}
        return response_body, 200

    else:
        response_body = {"message": "User with this session id not found "}
        return response_body, 404


@app.route('/validate', methods=['POST', 'GET'])
def validate():
    result = request.form
    session_id = result["session_id"]
    print('In validate route')
    quer = AuthManager.query.get(session_id)

    if quer:
        response_body = {
            "message": "Successfully get role",
            "session_id": session_id,
            "role": quer,
        }
        return response_body, 409

    else:
        response_body = {
            "message": "Not found",
            "session_id": session_id}
        return response_body, 404


@app.route('/add_user', methods=['POST'])
def add_user():
    # db.create_all()
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

    # except BaseException:
    #     response_body = {"message": "Error occured while adding user"}
    #     return response_body, 404


@app.route('/delete_user', methods=['POST', 'GET'])
def delete_user():
    result = request.form
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

    result = request.form
    # name = result["name"]

    user_id = result["user_id"]
    quer = db.session.query(User).filter_by(User.user_id == user_id).first()
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
