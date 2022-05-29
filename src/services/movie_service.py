from flask import jsonify, Response
from bson.objectid import ObjectId
from bson import json_util
from utils.constants import *
from utils.helpers import *

# Post Movie
def save_movie(mongo, request):
    name = get_field(request, "name")
    year = get_field(request, "year")
    imageBG = get_field(request, "imageBG")
    imageCard = get_field(request, "imageCard")
    video = get_field(request, "video")
    duration = get_field(request, "duration")
    genreId = get_field(request, "genreId")
    sinopsis = get_field(request, "sinopsis")
    director = get_field(request, "director")
    idioms = get_field(request, "idioms")
    actors = get_field(request, "actors")

    if name and genreId:
        body = {
            "name": name,
            "year": year,
            "imageBG": imageBG,
            "imageCard": imageCard,
            "video": video,
            "duration": duration,
            "genreId": genreId,
            "sinopsis": sinopsis,
            "director": director,
            "idioms": idioms,
            "actors": actors,
        }
        _id = mongo.db.movies.insert_one({**body})
        response = jsonify({"_id": str(_id.inserted_id), **body})
        response.status_code = CREATED_CODE
        return response
    else:
        return error(request)


# Get All Movies
def get_all_movies(mongo):
    # movies = mongo.db.movies.find()
    movies = mongo.db.movies.aggregate(
        [
            {
                "$lookup": {
                    "from": "genres",
                    "localField": "genreId",
                    "foreignField": "_id",
                    "as": "genres",
                }
            }
        ]
    )
    print(movies)
    response = json_util.dumps(movies)
    response = remove_oid(response)
    return Response(response, mimetype="application/json")


# Get Movie by ID
def get_movie_by_id(mongo, id):
    movie = mongo.db.movies.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(movie)
    response = remove_oid(response)
    return Response(response, mimetype="application/json")


# Delete Movie by ID
def delete_movie_by_id(mongo, id):
    movieDeleted = mongo.db.movies.delete_one({"_id": ObjectId(id)})
    response = jsonify({"message": "Movie " + id + " Deleted Successfully"})
    response.status_code = 200
    return response


# Update Movie by ID
def update_movie_by_id(mongo, request, id):
    name = get_field(request, "name")
    year = get_field(request, "year")
    imageBG = get_field(request, "imageBG")
    imageCard = get_field(request, "imageCard")
    video = get_field(request, "video")
    duration = get_field(request, "duration")
    genreId = get_field(request, "genreId")
    sinopsis = get_field(request, "sinopsis")
    director = get_field(request, "director")
    idioms = get_field(request, "idioms")
    actors = get_field(request, "actors")

    body = {
        "name": name,
        "year": year,
        "imageBG": imageBG,
        "imageCard": imageCard,
        "video": video,
        "duration": duration,
        "genreId": genreId,
        "sinopsis": sinopsis,
        "director": director,
        "idioms": idioms,
        "actors": actors,
    }

    _id = mongo.db.movies.update_one({"_id": ObjectId(id)}, {"$set": {**body}})
    if _id.modified_count == 1:
        response = jsonify({"_id": id, **body})
        response.status_code = OK
        return response
    else:
        return error(request)
