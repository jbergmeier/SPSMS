from flask import Blueprint, render_template, abort, jsonify, request
from database.models import setup_db, App_User, db, PreBooking, Ad_Area, Ad_Category, Ad_Category_Area
from auth.auth import AuthError, requires_auth

prebookings = Blueprint("prebookings", __name__)

'''
###################################################
prebookings endpoints
###################################################
'''


@prebookings.route('/', methods=['POST'])
@requires_auth(permission='post:sales')
def add_prebooking(payload):
    req = request.get_json()
    req_user = req.get('id_user')
    req_area_category = req.get('id_area_category')

    if not req_user:
        abort(404)
    if not req_area_category:
        abort(404)
    try:
        new_prebooking = PreBooking(
            id_customer=req_user, id_area_category=req_area_category)
        new_prebooking.insert()

        return jsonify({
            "success": True,
            "prebooking": new_prebooking.long()
        })

    except:
        abort(422)


@prebookings.route('/', methods=['GET'])
@requires_auth(permission='get:sales')
def get_prebookings(payload):

    try:
        prebookings = PreBooking.query.all()
        #all_prebookings = [prebooking.short() for prebooking in prebookings]
        result = []
        result_area = []
        result_category = []

        for prebooking in prebookings:
            result_area = []
            result_category = []
            user = App_User.query.filter(
                App_User.id == prebooking.id_customer).first()

            categories = Ad_Category.query.join(
                Ad_Category_Area, Ad_Category_Area.id_category == Ad_Category.id).filter(Ad_Category_Area.id == prebooking.id_area_category).all()

            areas = Ad_Area.query.join(
                Ad_Category_Area, Ad_Category_Area.id_area == Ad_Area.id).filter(Ad_Category_Area.id == prebooking.id_area_category).all()

            for area in areas:
                result_area.append(area.long())

            for category in categories:
                result_category.append(category.long())

            result.append({"id": prebooking.id, "firstname": user.firstname, "company": user.company, "email": user.email,
                           "lastname": user.lastname, "bookingDate": prebooking.ad_date, "area": result_area, "category": result_category})
        return jsonify({
            "success": True,
            "prebookings": result
        })
    except:
        abort(422)


@prebookings.route('/<int:id>', methods=['GET'])
@requires_auth(permission='get:sales')
def get_single_prebooking(payload, id):

    try:
        prebooking = PreBooking.query.filter(PreBooking.id == id).first()
        result = []
        result_area = []
        result_category = []

        user = App_User.query.filter(
            App_User.id == prebooking.id_customer).first()

        categories = Ad_Category.query.join(
            Ad_Category_Area, Ad_Category_Area.id_category == Ad_Category.id).filter(Ad_Category_Area.id == prebooking.id_area_category).all()

        areas = Ad_Area.query.join(
            Ad_Category_Area, Ad_Category_Area.id_area == Ad_Area.id).filter(Ad_Category_Area.id == prebooking.id_area_category).all()

        for area in areas:
            result_area.append(area.long())

        for category in categories:
            result_category.append(category.long())

        result.append({"id": prebooking.id, "firstname": user.firstname, "company": user.company, "email": user.email,
                       "lastname": user.lastname, "bookingDate": prebooking.ad_date, "area": result_area, "category": result_category})
        return jsonify({
            "success": True,
            "prebookings": result
        })
    except:
        abort(422)

#  user = App_User.query.filter(App_User.id == id).first()
#     if not user:
#         abort(404)

#     groups = App_Group.query.filter(
#         App_Group.app_user.any(App_User.id == id)).all()
#     user_groups = [group.short() for group in groups]
#     try:
#         return jsonify({
#             "success": True,
#             "groups": user_groups
#         })
