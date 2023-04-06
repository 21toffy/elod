from datetime import datetime
from app import database
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class User(database.Model):
    __tablename__ = 'users'

    id = database.Column(database.Integer, autoincrement=True, primary_key=True)
    name = database.Column(database.String(100), nullable=False, unique=True)
    salary = database.Column(database.Integer, nullable=False)
    time_created = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    department = database.Column(database.String(100), nullable=False)

    def __repr__(self):
        return f'<User: {self.name}>'
    

class Department(database.Model):
    __tablename__ = 'departments'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), nullable=False)
    users = relationship('User', backref='department')

    def __repr__(self):
        return '<Department %r>' % self.name

class Tenure(database.Model):
    __tablename__ = 'tenures'

    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, ForeignKey('users.id'), nullable=False)
    department_id = database.Column(database.Integer, ForeignKey('departments.id'), nullable=False)
    years = database.Column(database.Integer, nullable=False)
    time_created = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Tenure %r>' % self.years
