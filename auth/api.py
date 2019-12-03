from flask import Flask, request, Response

from models.models import User
from run import db, app


@app.route('/User', methods=['POST'])
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


@app.route('/User', methods=['DELETE'])
def delete_user():
    result = request.form
    user_id = result["user_id"]
    user = db.session.query(User).filter_by(id=user_id).first()
    if user:
        db.session.delete(user)
        db.commit()
    else:
        return Response(status=404)


@app.route('/User', methods=['GET'])
def get_user():

    result = request.form

    user_id = result["user_id"]
    quer = db.session.query(User).filter_by(id=user_id).first()
    db.session.commit()
    db.session.close()

    if quer:
        response_body = {"message": "User exists with this id"}
        # return response_body, 200
        return Response(status=200)

    else:
        return Response(status=404)


@app.route('/User', methods=['PUT'])
def update_user():
    result = request.form
    user_id = result["user_id"]
    return Response(status=200)

    # quer = db.session.query(User).filter_by(id=user_id).first()
    # # db.session.commit()
    # # db.session.close()
    #
    # if quer:
    #     quer.name = "talha"
    #     # quer = db.session.query(User).filter_by(id=user_id).update(name=result["name"])
    #     db.session.commit()
    #     db.session.close()
    #     return Response(status=200)
    #
    # else:
    #     return Response(status=404)
