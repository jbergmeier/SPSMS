from flask import Blueprint, render_template, abort, jsonify, request
from database.models import setup_db, Ad_Category
from auth.auth import AuthError, requires_auth


categories = Blueprint("categories", __name__)

'''
###################################################
category endpoints
###################################################
'''


@categories.route('/', methods=['GET'])
def show_categories():
    all_categories = Ad_Category.query.all()
    if not all_categories:
        return jsonify({
            "success": True,
            "message": "No category are setup in the DB"
        })
    try:
        categories = [category.short() for category in all_categories]

        return jsonify({
            "success": True,
            "categories": categories
        })
    except:
        abort(422)


@categories.route('/<int:id>', methods=['GET'])
def get_single_category(id):
    single_category = Ad_Category.query.filter(Ad_Category.id == id).first()
    if not single_category:
        abort(404)
    try:
        return jsonify({
            "success": True,
            "categories": single_category.long()
        })
    except:
        abort(422)


@categories.route('/', methods=['POST'])
def create_category():
    req = request.get_json()
    if not req.get('code'):
        abort(400)

    try:
        req_name = req.get('name')
        req_code = req.get('code')
        req_mm_min = req.get('mm_min')
        req_mm_max = req.get('mm_max')
        req_column_min = req.get('column_min')
        req_column_max = req.get('column_max')
        req_notes = req.get('notes')
        check_category_code = Ad_Category.query.filter(
            Ad_Category.code == req_code).all()

        if check_category_code:
            return jsonify({
                "success": False,
                "message": "Category Code already exists"
            })

        new_category = Ad_Category(name=req_name, code=req_code, mm_min=req_mm_min, mm_max=req_mm_max,
                                   column_min=req_column_min, column_max=req_column_max, notes=req_notes)
        new_category.insert()

        return jsonify({
            "success": True,
            "category": new_category.short()
        })
    except:
        abort(422)


@categories.route('/<int:id>', methods=['PATCH'])
def patch_category(id):
    single_category = Ad_Category.query.filter(Ad_Category.id == id).first()
    if not single_category:
        abort(404)

    req = request.get_json()

    try:
        if 'name' in req:
            single_category.name = req.get('name')

        if 'code' in req:
            single_category.code = req.get('code')

        if 'mm_min' in req:
            single_category.mm_min = req.get('mm_min')

        if 'mm_max' in req:
            single_category.mm_max = req.get('mm_max')

        if 'column_min' in req:
            single_category.column_min = req.get('column_min')

        if 'column_max' in req:
            single_category.column_max = req.get('column_max')

        if 'notes' in req:
            single_category.notes = req.get('notes')

        single_category.update()

        return jsonify({
            "success": True,
            "Category": single_category.long()
        })

    except:
        abort(422)


@categories.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    single_category = Ad_Category.query.filter(Ad_Category.id == id).first()
    if not single_category:
        abort(404)
    try:
        delete_category = Ad_Category.query.filter(
            Ad_Category.id == id).first()
        delete_category.delete()

        return jsonify({
            "success": True,
            "deleted Category code": delete_category.code
        })

    except:
        abort(422)
