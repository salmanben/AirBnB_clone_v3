#!/usr/bin/python3
'''Create a new view for Amenity objects that handles
all default RESTFul API actions'''
from flask import jsonify, abort, request
from models import storage
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('/api/v1/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    '''Retrieves the list of all Amenity objects'''
    amenities = storage.all(Amenity).values()
    amenities = [amenity.to_dict() for amenity in amenities]
    return jsonify(amenities)

@app_views.route('/api/v1/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    '''Retrieve an Amenity object'''
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        return jsonify(amenity.to_dict())
    else:
        abort(404)

@app_views.route('/api/v1/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    '''Delete an Amenity object'''
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        storage.delete(amenity)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)

@app_views.route('/api/v1/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    '''Create an Amenity object'''
    if not request.get_json():
        abort(400, message='Not a JSON')
    if 'name' not in request.get_json():
        abort(400, message='Missing name')
    amenity = Amenity(**request.get_json())
    amenity.save()
    return jsonify(amenity.to_dict()), 201

@app_views.route('/api/v1/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
    '''Update an Amenity object'''
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    else:
        data = request.get_json()
        if not data:
            abort(400, message='Not a JSON')

        ignore_keys = ['id', 'created_at', 'updated_at']
        for key, value in data.items():
            if key not in ignore_keys:
                setattr(amenity, key, value)
        amenity.save()
        return jsonify(amenity.to_dict()), 200
