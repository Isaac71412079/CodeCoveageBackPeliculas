from flask import jsonify, Response
from bson.objectid import ObjectId
from bson import json_util
from utils.constants import *
import re

# Post User
def save_user(mongo, request):
    username = get_field(request, "username")
    email = get_field(request, "email")
    password = get_field(request, "password")
    isAdmin = get_field(request, "isAdmin")

    if username and email and password:
        body = {
            "username": username,
            "password": password,
            "email": email,
            "isAdmin": isAdmin,
        }
        _id = mongo.db.users.insert_one({**body})
        response = jsonify({"_id": str(_id.inserted_id), **body})
        response.status_code = CREATED_CODE
        return response
    else:
        return error(request)


# Get All Users
def get_all_users(mongo):
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    response = remove_oid(response)
    return Response(response, mimetype="application/json")


# Get User by ID
def get_user_by_id(mongo, id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(user)
    response = remove_oid(response)
    return Response(response, mimetype="application/json")


# Delete User by ID
def delete_user_by_id(mongo, id):
    userDeleted = mongo.db.users.delete_one({"_id": ObjectId(id)})
    response = jsonify({"message": "User " + id + " Deleted Successfully"})
    response.status_code = 200
    return response


# Helpers
def error(request):
    message = {
        "message": "Oops! Something went wrong - " + request.url,
        "status": ERROR_CODE,
    }
    response = jsonify(message)
    response.status_code = ERROR_CODE
    return response


def get_field(request, field):
    return request.json.get(field, None)


def remove_oid(string):
    while True:
        pattern = re.compile('{\s*"\$oid":\s*("[a-z0-9]{1,}")\s*}')
        match = re.search(pattern, string)
        if match:
            string = string.replace(match.group(0), match.group(1))
        else:
            return string
