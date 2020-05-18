from flask import Blueprint, render_template, abort, jsonify, request
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
        groups = [group.short() for group in all_groups]
        return jsonify({
            "success": True,
            "groups": groups
        })
    except:
        abort(422)


@groups.route('/createGroup', methods=['POST'])
def create_group():
    req = request.get_json()
    try:
        req_name = req.get('name')
        new_group = App_Group(name=req_name)
        new_group.insert()

        return jsonify({
            "success": True,
            "group": new_group.short()
        })
    except:
        abort(422)


@groups.route('/<int:id>', methods=['DELETE'])
def delete_group(id):
    group = App_Group.query.filter(App_Group.id == id).first()
    if not group:
        abort(404)
    try:
        group.delete()
        return jsonify({
            "success": True,
            "group": group.short()
        })
    except:
        abort(422)


@groups.route('/<int:id>/users', methods=['GET'])
def get_users_in_group(id):
    pass
