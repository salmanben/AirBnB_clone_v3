#!/usr/bin/python3
''' Create a new view for city objects'''

from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City
from flask import abort, request, jsonify


@app_views.route('/states/<id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities(id):
    ''' Retrieves a cities objects of a state'''
    state = storage.get(State, id)
    if not state:
        abort(404)
    cities = state.cities
    cities_dict = [city.to_dict() for city in cities]
    return jsonify(cities_dict), 200


@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    ''' deletes a State objects from the database'''
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict()), 200


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    ''' delete a city objects from the database'''
    city = storage.get(City, city_id)
    if not city:
        abort(404)

