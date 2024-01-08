#!/usr/bin/python3
"""api place_amenities"""

from flask import abort, make_response, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User
import json
from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")


@app_views.route("/places/<id_place>/amenities", methods=["GET"],
                 strict_slashes=False)
def get_place_amenities(id_place):
    """retrieves all amenities of place id object"""
    place = storage.get(Place, id_place)
    amenitiesList = []
    if not place:
        abort(404)
    if storage_t == "db":
        for amenity in place.amenities:
            amenitiesList.append(amenity.to_dict())
    else:
        for id in place.amenity_ids:
            amenity = storage.get(Amenity, id)
            amenitiesList.append(amenity.to_dict())
    res = amenitiesList
    response = make_response(json.dumps(res), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@app_views.route("/places/<place_id>/amenities/<amenity_id>",
                 methods=["DELETE"])
def delete_place_amenity(place_id, amenity_id):
    """deletes amenity link to place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if storage_t == "db":
        if amenity not in place.amenities:
            abort(404)
        place.amenities.remove(amenity)
    else:
        if amenity_id not in place.amenity_ids:
            abort(404)
        place.amenity_ids.remove(amenity_id)
    storage.save()
    res = {}
    response = make_response(json.dumps(res), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@app_views.route("/places/<place_id>/amenities/<amenity_id>", methods=["POST"],
                 strict_slashes=False)
def create_place_amenity(place_id, amenity_id):
    """links amenity to place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if storage_t == "db":

