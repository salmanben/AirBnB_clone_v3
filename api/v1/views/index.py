#!/usr/bin/python3
"""api index"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", strict_slashes=False, methods=['GET'])
def status():
    """api status"""
    return jsonify({"status": "OK"}), 200

@app_views.route("/stats", strict_slashes=False, methods=['GET'])
def stats():
    """api states"""
    count = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(count)


