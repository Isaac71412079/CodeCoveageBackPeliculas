from flask import Flask, request, Response
from flask_pymongo import PyMongo
from services.user_service import *
from services.movie_service import *
from utils.constants import *

app = Flask(__name__)

app.config["MONGO_URI"] = DB_URI
mongo = PyMongo(app)


@app.route(USERS_PATH, methods=["POST"])
def create_users():
    response = save_user(mongo, request)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route(USERS_PATH, methods=["GET"])
def get_users():
    response = get_all_users(mongo)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route(USERS_PATH + ID, methods=["GET"])
def get_user(id):
    response = get_user_by_id(mongo, id)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route(USERS_PATH + ID, methods=["DELETE"])
def delete_user(id):
    response = delete_user_by_id(mongo, id)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# MOVIES


@app.route(MOVIES_PATH, methods=["POST"])
def create_movie():
    response = save_movie(mongo, request)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route(MOVIES_PATH, methods=["GET"])
def get_movies():
    response = get_all_movies(mongo)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route(MOVIES_PATH + ID, methods=["GET"])
def get_movie(id):
    response = get_movie_by_id(mongo, id)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route(MOVIES_PATH + ID, methods=["DELETE"])
def delete_movie(id):
    response = delete_movie_by_id(mongo, id)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    app.run(debug=True)
