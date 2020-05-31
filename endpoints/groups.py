from flask import Blueprint, render_template, abort, jsonify, request
from database.models import setup_db, App_User, App_Group
from auth.auth import AuthError, requires_auth

groups = Blueprint("groups", __name__)

'''
###################################################
groups endpoints
###################################################
'''


@groups.route('/', methods=['GET'])
@requires_auth(permission='get:group')
def get_groups(payload):
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


@groups.route('/', methods=['POST'])
@requires_auth(permission='post:group')
def create_group(payload):
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
@requires_auth(permission='post:group')
def delete_group(payload, id):
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
@requires_auth(permission='get:group')
def get_users_in_group(payload, id):
    users_per_group = App_Group.query.filter(App_Group.id == id).all()
    if not users_per_group:
        abort(404)
    try:
        return jsonify({
            "success": True,
            # "users": users_per_group.short()
        })
    except:
        abort(422)
