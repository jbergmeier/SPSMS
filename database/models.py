from sqlalchemy import Column, String, Integer, create_engine, DateTime, Float, ForeignKey, Boolean
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate, MigrateCommand
import datetime
import os

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
N-M Table for User/Group
'''
app_user_group = db.Table('app_user_group',
                          db.Column('app_user_id', db.Integer,
                                    db.ForeignKey('app_user.id')),
                          db.Column('app_group_id', db.Integer,
                                    db.ForeignKey('app_group.id'))
                          )

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


'''
Groups for Users of the Database incl. Customers
'''


class App_Group(db.Model):
    __tablename__ = 'app_group'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    app_user = db.relationship("App_User",
                               secondary=app_user_group, backref=db.backref('groups'), lazy=True)

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
            'name': self.name
        }

    def __repr__(self):
        return json.dumps(self.short())


class Ad_Area(db.Model):
    __tablename__ = 'ad_area'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=True)
    gp_mm_price = Column(Float, nullable=True)
    gp_mm_price_text = Column(Float, nullable=True)
    dp_mm_price = Column(Float, nullable=True)
    dp_mm_price_text = Column(Float, nullable=True)
    # fixed_prices = db.relationship('Ad_Fixed_Price', backref='ad_area', lazy=True)
    category_area = db.relationship(
        'Ad_Category_Area', backref='ad_area', lazy=True)

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
            'name': self.name
        }

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'gp_mm_price': self.gp_mm_price,
            'gp_mm_price_text': self.gp_mm_price_text,
            'dp_mm_price': self.dp_mm_price,
            'dp_mm_price_text': self.dp_mm_price_text
        }

    def __repr__(self):
        return json.dumps(self.short())


# class Ad_Fixed_Price(db.Model):
#     __tablename__ = 'ad_fixed_price'

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     gp_price = Column(Float, nullable=True)
#     dp_price = Column(Float, nullable=True)
#     notes = Column(String, nullable=True)
#     id_ad_area = Column(Integer, ForeignKey('ad_area.id'), nullable=False)

#     def insert(self):
#         db.session.add(self)
#         db.session.commit()

#     def update(self):
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()

#     def short(self):
#         return {
#             'id': self.id,
#             'name': self.name
#         }

#     def long(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'gp_price': self.gp_price,
#             'dp_price': self.dp_price,
#             'notes': self.notes,
#             'id_ad_area': self.id_ad_area
#         }

#     def __repr__(self):
#         return json.dumps(self.short())


class Ad_Category(db.Model):
    __tablename__ = 'ad_category'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    mm_min = Column(Integer, nullable=True)
    mm_max = Column(Integer, nullable=True)
    column_min = Column(Integer, nullable=True)
    column_max = Column(Integer, nullable=True)
    notes = Column(String, nullable=True)
    isFixedPrice = Column(Boolean, nullable=False, default=0)
    active = Column(Boolean, nullable=False, default=0)
    category_area = db.relationship(
        'Ad_Category_Area', backref='ad_category', lazy=True)

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
            'code': self.code,
            'name': self.name
        }

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'mm_min': self.mm_min,
            'mm_max': self.mm_max,
            'column_min': self.column_min,
            'column_max': self.column_max,
            'notes': self.notes
        }

    def __repr__(self):
        return json.dumps(self.short())


class Ad_Category_Area(db.Model):
    __tablename__ = 'ad_category_area'

    id = Column(Integer, primary_key=True)
    valid_from = Column(DateTime, nullable=False)
    valid_to = Column(DateTime, nullable=False)
    activated = Column(Boolean, nullable=False, default=0)
    id_category = Column(Integer, ForeignKey('ad_category.id'), nullable=False)
    id_area = Column(Integer, ForeignKey('ad_area.id'), nullable=False)
