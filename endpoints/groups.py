from flask import Blueprint, render_template, abort, jsonify
from database.models import setup_db, App_User, App_Group

groups = Blueprint("groups", __name__)

'''
###################################################
groups endpoints
###################################################
'''


@groups.route('/', methods=['GET'])
def get_groups():
    all_groups = App_Group.query.all()
    if not all_groups:
        return jsonify({
            "success": True,
            "message": "No groups are setup in the DB"
        })
    try:
        pass
    except:
        abort(422)


@groups.route('/createGroup', methods=['POST'])
def create_group():
    pass


@groups.route('/<int:id>', methods=['DELETE'])
def delete_group(id):
    pass


@groups.route('/<int:id>/users', methods=['GET'])
def get_users_in_group(id):
    pass
