#!/usr/bin/python3
''' Create a new view for State objects'''

from api.v1.views import app_views
from models import storage
from models.state import State
from flask import abort, request, jsonify


@app_views.route('/states', methods=['GET'],
                 strict_slashes=False)
def get_states():
    ''' Retrieves the list of all State objects'''
    states = storage.all(State).values()
    states_obj = [state. to_dict() for state in states]
    return jsonify(states_obj), 200


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    ''' Retrieves a State objects from the database'''
    state = storage.get(State, state_id)
    if not state:
        return abort(404)
    state_dict = state.to_dict()
    return jsonify(state_dict), 200


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    ''' deletes a State objects from the database'''
    state = storage.get(State, state_id)
    if not state:
        return abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'],
                 strict_slashes=False)
def create_state():
    ''' create a State objects'''
    json_data = request.get_json()
    if not json_data:
        return abort(400, "Not a JSON")
    if 'name' not in json_data:
        abort(400, "Missing name")
    state = State(**json_data)
    state.save()
    state_dict = state.to_dict()
    return jsonify(state_dict), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """ update a state"""
    state = storage.get(State, state_id)
    if not state:
        abort(404, "Not found")
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")

