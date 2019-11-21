from datetime import datetime

from mongoengine import *
from sqlalchemy import Column, String, Boolean, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

from init import db


class AuthManager(db.Model):
    __tablename__ = 'auth_table'
    user_id = StringField()
    session_id = StringField()
    role = StringField(choices=["student", "teacher"])


class User(db.Model):
    __tablename__ = 'users'
    user_id = Column('user_id', Integer, primary_key=True)
    name = Column('name', String(50))
    age = Column('age', String(100))
    grade = Column('grade', Integer)
    department = Column('department', String(100))
    password = Column('password', String(100))
    # verified = Column('verified', Boolean)
    # date_created = Column('date_created', DateTime, default=datetime.now)

    def __init__(self, name, age, grade, department, password):
        self.name = name
        self.age = age
        self.grade = grade
        self.department = department
        self.password = password
        # self.verified = verified

