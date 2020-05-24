from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.sql import exists
from flask_migrate import Migrate, MigrateCommand
import logging
import os
import datetime
from database.models import setup_db, App_User, db
from auth.auth import AuthError, requires_auth
from endpoints.users import users
from endpoints.groups import groups
from endpoints.categories import categories
from endpoints.areas import areas
from endpoints.prebooking import prebooking

# db.drop_all()
# db.create_all()


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def default_route():
        print(request.get_data())
        return "<h1>Welcome to SPSMS Backend</h1>"

    '''
    ###################################################
    user endpoints
    ###################################################
    '''
    app.register_blueprint(users, url_prefix='/users')

    '''
    ###################################################
    groups endpoints
    ###################################################
    '''
    app.register_blueprint(groups, url_prefix='/groups')

    '''
    ###################################################
    category endpoints
    ###################################################
    '''
    app.register_blueprint(categories, url_prefix='/categories')

    '''
    ###################################################
    area endpoints + category_area
    ###################################################
    '''
    app.register_blueprint(areas, url_prefix='/areas')

    '''
    ###################################################
    prebooking
    ###################################################
    '''
    app.register_blueprint(prebooking, url_prefix='/prebooking')

    '''
    ###################################################
    Errorhandler for different Cases
    ###################################################
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
