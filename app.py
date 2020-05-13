from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.sql import exists
from flask_migrate import Migrate, MigrateCommand
import logging
import os
from models import setup_db, App_User
from auth import AuthError


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/createUser', methods=['POST'])
    def create_user():
        req = request.get_json()
        try:
            req_email = req.get('email')
            req_firstname = req.get('firstname')
            req_lastname = req.get('lastname')
            req_company = req.get('company')
            req_address = req.get('address')
            req_postalcode = req.get('postalcode')
            req_postalplace = req.get('postalplace')
            req_country = req.get('country')

            new_user = App_User(firstname=req_firstname, lastname=req_lastname, email=req_email, company=req_company, address=req_address,
                                postalcode=req_postalcode, postalplace=req_postalplace, country=req_country)
            print(new_user)
            new_user.insert()

            return jsonify({
                "success": True,
                "App_User": {
                    "firstname": req_firstname,
                    "lastname": req_lastname,
                    "email": req_email
                }
            })
        except:
            abort(422)

    @app.route('/users', methods=['GET'])
    def get_users():
        all_users = App_User.query.all()
        if not all_users:
            return jsonify({
                "success": True,
                "message": "No users are setup in the DB"
            })
        try:
            users = [user.short() for user in all_users]

            return jsonify({
                "success": True,
                "users": users
            })
        except:
            abort(422)

    @app.route('/users/<int:id>', methods=['GET'])
    def get_single_user(id):
        single_user = App_User.query.filter(App_User.id == id).all()
        if not single_user:
            abort(404)
        try:
            user_result = [user.short() for user in single_user]
            return jsonify({
                "success": True,
                "user": user_result
            })
        except:
            abort(422)

    '''
    Errorhandler for different Cases
    '''
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "Access Forbidden"
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource not found"
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "The method is not allowed for the requested URL!"
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable Entity"
        }), 422

    @app.errorhandler(500)
    def serverError(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    @app.errorhandler(AuthError)
    def auth_error(e):
        return jsonify({
            "success": False,
            "error": e.status_code,
            "message": e.error
        }), e.status_code
    return app


app = create_app()

if __name__ == '__main__':
    app.run()
