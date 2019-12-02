import uuid

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from run import db


class User(db.Model):
    __tablename__ = 'users'
    id = Column('user_id', Integer, primary_key=True)
    name = Column('name', String(50))
    age = Column('age', String(100))
    grade = Column('grade', Integer)
    department = Column('department', String(100))
    password = Column('password', String(100))
    auth_manager = db.relationship('AuthManager', backref='user', lazy=True)

    # posts = db.relationship('Post', backref='poster', lazy='dynamic')

    # auth_manager = relationship("AuthManager", uselist=False, backref='user', cascade='delete_all')

    def __init__(self, name, age, grade, department, password):
        self.name = name
        self.age = age
        self.grade = grade
        self.department = department
        self.password = password
        # self.verified = verified
