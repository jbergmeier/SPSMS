from flask import Blueprint, render_template, abort, jsonify, request
from database.models import setup_db, Ad_Area, Ad_Category_Area, Ad_Fixed_Price
from auth.auth import AuthError, requires_auth

areas = Blueprint("areas", __name__)

'''
###################################################
areas endpoints
###################################################
'''


@areas.route('/', methods=['GET'])
def show_areas():
    all_areas = Ad_Area.query.all()
    if not all_areas:
        return jsonify({
            "success": True,
            "message": "No area are setup in the DB"
        })
    try:
        areas = [area.short() for area in all_areas]

        return jsonify({
            "success": True,
            "areas": areas
        })
    except:
        abort(422)


@areas.route('/<int:id>', methods=['GET'])
def get_single_area(id):
    single_area = Ad_Area.query.filter(Ad_Area.id == id).first()
    if not single_area:
        abort(404)
    try:
        return jsonify({
            "success": True,
            "area": single_area.long()
        })
    except:
        abort(422)


@areas.route('/', methods=['POST'])
def create_area():
    req = request.get_json()
    if not req.get('code'):
        abort(400)

    try:
        req_name = req.get('name')
        req_code = req.get('code')
        req_gp_mm_price = req.get('gp_mm_price')
        req_gp_mm_price_text = req.get('gp_mm_price_text')
        req_dp_mm_price = req.get('dp_mm_price')
        req_dp_mm_price_text = req.get('dp_mm_price_text')

        check_area_code = Ad_Area.query.filter(
            Ad_Area.code == req_code).all()

        if check_area_code:
            return jsonify({
                "success": False,
                "message": "Area Code already exists"
            })

        new_area = Ad_Area(name=req_name, code=req_code, gp_mm_price=req_gp_mm_price, gp_mm_price_text=req_gp_mm_price_text,
                           dp_mm_price=req_dp_mm_price, dp_mm_price_text=req_dp_mm_price_text)
        new_area.insert()

        return jsonify({
            "success": True,
            "area": new_area.short()
        })
    except:
        abort(422)


@areas.route('/<int:id>', methods=['PATCH'])
def patch_area(id):
    single_area = Ad_Area.query.filter(Ad_Area.id == id).first()
    if not single_area:
        abort(404)

    req = request.get_json()

    try:
        if 'name' in req:
            single_area.name = req.get('name')

        if 'code' in req:
            single_area.code = req.get('code')

        if 'gp_mm_price' in req:
            single_area.gp_mm_price = req.get('gp_mm_price')

        if 'gp_mm_price_text' in req:
            x
            single_area.gp_mm_price_text = req.get('gp_mm_price_text')

        if 'dp_mm_price' in req:
            single_area.dp_mm_price = req.get('dp_mm_price')

        if 'dp_mm_price_text' in req:
            single_area.dp_mm_price_text = req.get('dp_mm_price_text')

        single_area.update()

        return jsonify({
            "success": True,
            "Area": single_area.long()
        })

    except:
        abort(422)


@areas.route('/<int:id>', methods=['DELETE'])
def delete_area(id):
    single_area = Ad_Area.query.filter(Ad_Area.id == id).first()
    if not single_area:
        abort(404)
    try:
        delete_area = Ad_Area.query.filter(
            Ad_Area.id == id).first()
        delete_area.delete()

        return jsonify({
            "success": True,
            "deleted Area code": delete_area.code
        })

    except:
        abort(422)


'''
###################################################
fixedprices endpoints
###################################################
'''


@areas.route('/<int:id>/fixedPrices', methods=['GET'])
def show_fixedPrices_for_area(id):
    single_area = Ad_Area.query.filter(Ad_Area.id == id).first()
    if not single_area:
        abort(404)

    all_fixed_Prices_for_area = Ad_Fixed_Price.query.filter(
        Ad_Fixed_Price.id_ad_area == id).all()
    if not all_fixed_Prices_for_area:
        return jsonify({
            "success": True,
            "message": "No fixed prices for area in the DB"
        })

    try:
        fixedPrices = [area.long()
                       for area in all_fixed_Prices_for_area]

        return jsonify({
            "success": True,
            "area": single_area.short(),
            "fixedPrices": fixedPrices
        })
    except:
        abort(422)


@areas.route('/<int:id>/fixedPrices/<int:id_fixedPrice>', methods=['GET'])
def get_single_fixedPrice_for_area(id, id_fixedPrice):
    single_fixed_price_for_area = Ad_Fixed_Price.query.filter(
        Ad_Fixed_Price.id == id_fixedPrice).filter(Ad_Fixed_Price.id_ad_area == id).first()
    if not single_fixed_price_for_area:
        abort(404)

    try:
        return jsonify({
            "success": True,
            "area": single_fixed_price_for_area.long()
        })
    except:
        abort(422)


@areas.route('/<int:id>/fixedPrices/<int:id_fixedPrice>', methods=['PATCH'])
def patch_fixed_price_for_area(id, id_fixedPrice):
    single_fixed_price_for_area = Ad_Fixed_Price.query.filter(
        Ad_Fixed_Price.id == id_fixedPrice).filter(Ad_Fixed_Price.id_ad_area == id).first()
    if not single_fixed_price_for_area:
        abort(404)

    req = request.get_json()

    try:
        if 'name' in req:
            single_fixed_price_for_area.name = req.get('name')

        if 'dp_price' in req:
            single_fixed_price_for_area.dp_price = req.get('dp_price')

        if 'gp_price' in req:
            single_fixed_price_for_area.gp_price = req.get('gp_price')

        if 'notes' in req:
            single_fixed_price_for_area.notes = req.get('notes')

        single_fixed_price_for_area.update()

        return jsonify({
            "success": True,
            "Area": single_fixed_price_for_area.long()
        })

    except:
        abort(422)


@areas.route('/<int:id>/fixedPrices', methods=['POST'])
def create_fixedPrice_for_area(id):
    single_area = Ad_Area.query.filter(Ad_Area.id == id).first()
    if not single_area:
        abort(404)
    req = request.get_json()

    try:
        req_name = req.get('name')
        req_gp_price = req.get('gp_price')
        req_dp_price = req.get('dp_price')
        req_notes = req.get('notes')

        print(req_dp_price, " ", req_name)

        new_fixedPrice = Ad_Fixed_Price(name=req_name, gp_price=req_gp_price, dp_price=req_dp_price, notes=req_notes,
                                        id_ad_area=id)
        new_fixedPrice.insert()

        return jsonify({
            "success": True,
            "area id": id,
            "fixedPrice": new_fixedPrice.short()
        })
    except:
        abort(422)


@areas.route('/<int:id>/fixedPrices/<int:id_fixedPrice>', methods=['DELETE'])
def delete_fixed_price_for_area(id, id_fixedPrice):
    single_fixed_price_for_area = Ad_Fixed_Price.query.filter(
        Ad_Fixed_Price.id == id_fixedPrice).filter(Ad_Fixed_Price.id_ad_area == id).first()
    if not single_fixed_price_for_area:
        abort(404)

    try:
        delete_fixed_price = Ad_Fixed_Price.query.filter(
            Ad_Fixed_Price.id == id_fixedPrice).filter(Ad_Fixed_Price.id_ad_area == id).first()
        delete_fixed_price.delete()

        return jsonify({
            "success": True,
            "deleted fixed Price": delete_fixed_price.id
        })

    except:
        abort(422)


'''
###################################################
category_area endpoints
###################################################
'''


@areas.route('/<int:id>/categories', methods=['GET'])
def show_category_for_area(id):
    single_area = Ad_Area.query.filter(Ad_Area.id == id).first()
    if not single_area:
        abort(404)

    all_fixed_Prices_for_area = Ad_Fixed_Price.query.filter(
        Ad_Fixed_Price.id_ad_area == id).all()
    if not all_fixed_Prices_for_area:
        return jsonify({
            "success": True,
            "message": "No fixed prices for area in the DB"
        })

    try:
        fixedPrices = [area.long()
                       for area in all_fixed_Prices_for_area]

        return jsonify({
            "success": True,
            "area": single_area.short(),
            "fixedPrices": fixedPrices
        })
    except:
        abort(422)


# @areas.route('/<int:id>/fixedPrices/<int:id_fixedPrice>', methods=['GET'])
# def get_single_fixedPrice_for_area(id, id_fixedPrice):
#     single_fixed_price_for_area = Ad_Fixed_Price.query.filter(
#         Ad_Fixed_Price.id == id_fixedPrice).filter(Ad_Fixed_Price.id_ad_area == id).first()
#     if not single_fixed_price_for_area:
#         abort(404)

#     try:
#         return jsonify({
#             "success": True,
#             "area": single_fixed_price_for_area.long()
#         })
#     except:
#         abort(422)


# @areas.route('/<int:id>/fixedPrices/<int:id_fixedPrice>', methods=['PATCH'])
# def patch_fixed_price_for_area(id, id_fixedPrice):
#     single_fixed_price_for_area = Ad_Fixed_Price.query.filter(
#         Ad_Fixed_Price.id == id_fixedPrice).filter(Ad_Fixed_Price.id_ad_area == id).first()
#     if not single_fixed_price_for_area:
#         abort(404)

#     req = request.get_json()

#     try:
#         if 'name' in req:
#             single_fixed_price_for_area.name = req.get('name')

#         if 'dp_price' in req:
#             single_fixed_price_for_area.dp_price = req.get('dp_price')

#         if 'gp_price' in req:
#             single_fixed_price_for_area.gp_price = req.get('gp_price')

#         if 'notes' in req:
#             single_fixed_price_for_area.notes = req.get('notes')

#         single_fixed_price_for_area.update()

#         return jsonify({
#             "success": True,
#             "Area": single_fixed_price_for_area.long()
#         })

#     except:
#         abort(422)


# @areas.route('/<int:id>/fixedPrices', methods=['POST'])
# def create_fixedPrice_for_area(id):
#     single_area = Ad_Area.query.filter(Ad_Area.id == id).first()
#     if not single_area:
#         abort(404)
#     req = request.get_json()

#     try:
#         req_name = req.get('name')
#         req_gp_price = req.get('gp_price')
#         req_dp_price = req.get('dp_price')
#         req_notes = req.get('notes')

#         print(req_dp_price, " ", req_name)

#         new_fixedPrice = Ad_Fixed_Price(name=req_name, gp_price=req_gp_price, dp_price=req_dp_price, notes=req_notes,
#                                         id_ad_area=id)
#         new_fixedPrice.insert()

#         return jsonify({
#             "success": True,
#             "area id": id,
#             "fixedPrice": new_fixedPrice.short()
#         })
#     except:
#         abort(422)


# @areas.route('/<int:id>/fixedPrices/<int:id_fixedPrice>', methods=['DELETE'])
# def delete_fixed_price_for_area(id, id_fixedPrice):
#     single_fixed_price_for_area = Ad_Fixed_Price.query.filter(
#         Ad_Fixed_Price.id == id_fixedPrice).filter(Ad_Fixed_Price.id_ad_area == id).first()
#     if not single_fixed_price_for_area:
#         abort(404)

#     try:
#         delete_fixed_price = Ad_Fixed_Price.query.filter(
#             Ad_Fixed_Price.id == id_fixedPrice).filter(Ad_Fixed_Price.id_ad_area == id).first()
#         delete_fixed_price.delete()

#         return jsonify({
#             "success": True,
#             "deleted fixed Price": delete_fixed_price.id
#         })

#     except:
#         abort(422)