from flask import Blueprint, render_template, abort, jsonify
from database.models import setup_db, App_User

users = Blueprint("users", __name__)

'''
###################################################
user endpoints
###################################################
'''


@users.route('/createUser', methods=['POST'])
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


@users.route('/', methods=['GET'])
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


@users.route('/<int:id>', methods=['GET'])
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


@users.route('/<int:id>', methods=['PATCH'])
def patch_user(id):
    single_user = App_User.query.filter(App_User.id == id).first()
    if not single_user:
        abort(404)

    req = request.get_json()

    try:
        if 'firstname' in req:
            single_user.firstname = req.get('firstname')

        if 'lastname' in req:
            single_user.lastname = req.get('lastname')

        if 'email' in req:
            single_user.email = req.get('email')

        if 'company' in req:
            single_user.company = req.get('company')

        if 'address' in req:
            single_user.address = req.get('address')

        if 'postalcode' in req:
            single_user.postalcode = req.get('postalcode')

        if 'postalplace' in req:
            single_user.postalplace = req.get('postalplace')

        if 'country' in req:
            single_user.country = req.get('country')

        single_user.updated_at = datetime.datetime.now()

        single_user.update()

        changed_user = [changed_user.long() for changed_user in App_User.query.filter(
            App_User.id == id).all()]

        return jsonify({
            "success": True,
            "User": changed_user
        })

    except:
        abort(422)


@users.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    single_user = App_User.query.filter(App_User.id == id).all()
    if not single_user:
        abort(404)
    try:
        delete_user = App_User.query.filter(App_User.id == id).first()
        delete_user.delete()

        return jsonify({
            "success": True,
            "deleted User id": delete_user.id
        })

    except:
        abort(422)
