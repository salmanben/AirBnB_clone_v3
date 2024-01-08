#!/usr/bin/python3
"""api reviews"""

from flask import abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.review import Review
from models.user import User
import json


@app_views.route("/places/<id_place>/reviews", methods=["GET"],
                 strict_slashes=False)
def get_reviews(id_place):
    """retrieves all reviews by place id object"""
    place = storage.get(Place, id_place)
    reviewsList = []
    if not place:
        abort(404)
    for review in place.reviews:
        reviewsList.append(review.to_dict())
    res = reviewsList
    response = make_response(json.dumps(res), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@app_views.route("/reviews/<id>", methods=["GET"])
def get_review(id):
    """retrieves reviews object with id"""
    review = storage.get(Review, id)
    if not review:
        abort(404)
    response_data = review.to_dict()
    response = make_response(json.dumps(response_data), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@app_views.route("/reviews/<id>", methods=["DELETE"])
def delete_review(id):
    """delets review with id"""
    review = storage.get(Review, id)
    if not review:
        abort(404)
    storage.delete(review)
    storage.save()
    res = {}
    response = make_response(json.dumps(res), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@app_views.route("/places/<id_place>/reviews", methods=["POST"],
                 strict_slashes=False)
def create_review(id_place):
    """inserts reviews if its valid json amd has correct key and state id"""
    missingIdMSG = "Missing user_id"
    missingTextMSG = "Missing text"
    place = storage.get(Place, id_place)
    if not place:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description='Not a JSON')
    if "user_id" not in data:
        abort(400, description=missingIdMSG)
    if not storage.get(User, data.get("user_id")):
        abort(404)
    if "text" not in data:
        abort(400, description=missingTextMSG)
    instObj = Review(**data)
    instObj.place_id = id_place

