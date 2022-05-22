from flask import jsonify, Response
from bson.objectid import ObjectId
from bson import json_util
from utils.constants import *
from utils.helpers import *

# Post Movie
def save_category(mongo, request):
    name = get_field(request, "name")
    if name and genreId:
        body = {
            "name": name
        }
        _id = mongo.db.categories.insert_one({**body})
        response = jsonify({"_id": str(_id.inserted_id), **body})
        response.status_code = CREATED_CODE
        return response
    else:
        return error(request)


# Get All Categories
def get_all_categories(mongo):
    categories = mongo.db.categories.find()
    response = json_util.dumps(categories)
    response = remove_oid(response)
    return Response(response, mimetype="application/json")


# Get Category by ID
def get_category_by_id(mongo, id):
    category = mongo.db.categories.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(category)
    response = remove_oid(response)
    return Response(response, mimetype="application/json")


# Delete Category by ID
def delete_category_by_id(mongo, id):
    categoryDeleted = mongo.db.categories.delete_one({"_id": ObjectId(id)})
    response = jsonify({"message": "Category " + id + " Deleted Successfully"})
    response.status_code = 200
    return response
