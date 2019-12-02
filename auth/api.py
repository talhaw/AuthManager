import uuid
import hashlib

from flask import Flask, request, Response

from run import db, app
from models.models import User


@app.route('/add_user', methods=['POST'])
def add_user():
    result = request.form

    name = result["name"]
    age = result["age"]
    grade = result["grade"]
    department = result["department"]
    password = result["password"]
    print('\nUser info = ', name, age, grade, department, password)
    new_user = User(name, age, grade, department, password)

    db.session.add(new_user)
    db.session.commit()

    response_body = {"message": "User added successfully"}
    return response_body, 200


@app.route('/delete_user', methods=['POST', 'GET'])
def delete_user():
    result = request.form
    user_id = result["user_id"]
    user = db.session.query(User).filter_by(id=user_id).first()
    if user:
        db.session.delete(user)
        db.commit()
    else:
        return Response(status=404)


@app.route('/get_user', methods=['POST', 'GET'])
def get_user():

    result = request.form

    user_id = result["user_id"]
    quer = db.session.query(User).filter_by(id=user_id).first()
    db.session.commit()
    db.session.close()

    if quer:
        response_body = {"message": "User exists with this id"}
        return response_body, 200

    else:
        return Response(status=404)
