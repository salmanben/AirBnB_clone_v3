#!/usr/bin/python3
''' Create a new view for Amenity objects'''

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from flask import abort, request, jsonify


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    ''' Retrieves the list of all Amenity objects'''
    amenities = storage.all(Amenity).values()
    amenities_obj = [amenity. to_dict() for amenity in amenities]
    return jsonify(amenities_obj), 200


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    ''' Retrieves a amenity objects from the database'''
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        return abort(404)
    amenity_dict = amenity.to_dict()
    return jsonify(amenity_dict), 200


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    ''' deletes an Amenity objects from the database'''
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        return abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


