from flask import request, Response
from flask_mail import Message

from models.models import User
from run import db, app, mail, celery


@app.route('/User', methods=['POST'])
def add_user():
    result = request.form
    email = result["email"]
    name = result["name"]
    age = result["age"]
    grade = result["grade"]
    department = result["department"]
    password = result["password"]

    new_user = User(email, name, age, grade, department, password)
    db.session.add(new_user)
    db.session.commit()
    #
    # msg = Message('Confirm Email', sender=app.config['MAIL_USERNAME'], recipients=[email])
    # msg.body = 'Your have been successfully registered to auth manager'
    # mail.send(msg)
    send_async_email.delay(email)

    return Response("Record added successfully", status=200)


@app.route('/User', methods=['DELETE'])
def delete_user():
    result = request.form
    user_id = result["user_id"]
    user = db.session.query(User).filter_by(id=user_id).first()

    if user:
        db.session.delete(user)
        db.session.commit()
        return Response(status=200)

    return Response(status=404)


@app.route('/User', methods=['GET'])
def get_user():

    result = request.form

    user_id = result["user_id"]
    quer = db.session.query(User).filter_by(id=user_id).first()
    db.session.commit()
    db.session.close()

    if quer:
        return Response(status=200)

    return Response(status=404)


@app.route('/User', methods=['PUT'])
def update_user():
    result = request.form
    user_id = result["user_id"]
    name = result["name"]

    quer = db.session.query(User).filter_by(id=user_id).first()
    if quer:
        quer.name = name
        db.session.commit()
        db.session.close()
        return Response(status=200)

    else:
        return Response(status=404)


@celery.task(name='auth.api.send_async_email')
def send_async_email(email):
    msg = Message('Confirm Email', sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.body = 'Your have been successfully registered to auth manager'
    with app.app_context():
        mail.send(msg)
