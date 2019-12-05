from sqlalchemy import Column, String, Integer

from run import db


class User(db.Model):
    __tablename__ = 'users'
    id = Column('user_id', Integer, primary_key=True)
    email = Column('email', String(50))
    name = Column('name', String(50))
    age = Column('age', String(100))
    grade = Column('grade', Integer)
    department = Column('department', String(100))
    password = Column('password', String(100))

    def __init__(self, email, name, age, grade, department, password):
        self.email = email
        self.name = name
        self.age = age
        self.grade = grade
        self.department = department
        self.password = password
