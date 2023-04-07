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
    department_id = database.Column(database.Integer, ForeignKey('departments.id'), nullable=True)

    def __repr__(self):
        return f'<User: {self.name}>'
    def total_tenure(self):
        tenures = Tenure.query.filter_by(user_id=self.id).all()
        return sum(tenure.years for tenure in tenures)

     
    # def total_tenure(self):
    #     tenures = self.tenures.all()
    #     return sum(tenure.years for tenure in tenures)
    def get_years_in_department(self, department_name):
        years_in_department = 0
        for tenure in self.tenures:
            if tenure.department.name == department_name:
                years_in_department += tenure.years
        return years_in_department


class Department(database.Model):
    __tablename__ = 'departments'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), nullable=False)
    users = relationship('User', backref='department')

    def __repr__(self):
        return '<Department %r>' % self.name
    @classmethod
    def get_total_tenure(cls):
        total_tenure = {}
        for department in cls.query.all():
            for tenure in department.tenures:
                user = tenure.user
                years = tenure.years
                if user.name not in total_tenure:
                    total_tenure[user.name] = years
                else:
                    total_tenure[user.name] += years
        return total_tenure

class Tenure(database.Model):
    __tablename__ = 'tenures'

    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, ForeignKey('users.id'), nullable=False)
    department_id = database.Column(database.Integer, ForeignKey('departments.id'), nullable=False)
    years = database.Column(database.Integer, nullable=False)
    time_created = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)


    user = relationship('User', backref='tenures')
    department = relationship('Department', backref='tenures')

    def __repr__(self):
        return '<Tenure %r>' % self.years
