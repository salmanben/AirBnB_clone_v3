#!/usr/bin/python3
"""create views for api places"""

from flask import abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity
import json


@app_views.route("/cities/<id>/places", methods=["GET"],
                 strict_slashes=False)
def get_places(id):
    """retrieves all places by city id object"""
    city = storage.get(City, id)
    if not city:
        abort(404)
    places = [place.to_dict() for place in city.places]
    res = places
    response = make_response(json.dumps(res), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@app_views.route("/places/<id>", methods=["GET"])
def get_place(id):
    """retrieves places object with id"""
    place = storage.get(Place, id)
    if not place:
        abort(404)
    res = place.to_dict()
    response = make_response(json.dumps(res), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@app_views.route("/places/<id>", methods=["DELETE"])
def delete_place(id):
    """delets city with id"""
    place = storage.get(Place, id)
    if not place:
        abort(404)
    storage.delete(place)
    storage.save()
    res = {}
    response = make_response(json.dumps(res), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@app_views.route("/cities/<id>/places", methods=["POST"],
                 strict_slashes=False)
def post_place(id):
    """inserts place if its valid json and has correct keys and city id"""
    missingMSG = "Missing name"
    userMissingMsg = "Missing user_id"
    city = storage.get(City, id)
    if not city:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if "user_id" not in request.get_json():
        abort(400, description=userMissingMsg)
    data = request.get_json()
    user = storage.get(User, data["user_id"])
    if not user:
        abort(404)
    if "name" not in request.get_json():
        abort(400, description=missingMSG)
    data["city_id"] = id
    place = Place(**data)
