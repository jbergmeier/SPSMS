from sqlalchemy import Column, String, Integer, create_engine, DateTime
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate, MigrateCommand
import datetime
import os

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Users of the Database incl. Customers
'''


class App_User(db.Model):
    __tablename__ = 'app_user'

    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    company = Column(String)
    email = Column(String, nullable=False)
    address = Column(String)
    postalcode = Column(String)
    postalplace = Column(String)
    country = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime)

    def __init__(self, firstname, lastname, company, email, address, postalcode, postalplace, country):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.email = email
        self.address = address
        self.postalcode = postalcode
        self.postalplace = postalplace
        self.country = country

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def short(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email
        }

    def long(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'company': self.company,
            'email': self.email,
            'address': self.address,
            'postalcode': self.postalcode,
            'postalplace': self.postalplace,
            'country': self.country
        }

    def __repr__(self):
        return json.dumps(self.short())
