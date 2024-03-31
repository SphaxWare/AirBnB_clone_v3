#!/usr/bin/python3
"""index.py for api status"""
from flask import jsonify
from . import app_views


@app_views.route('/status', strict_slashes=False)
def get_status():
    """Return API Status"""
    return jsonify({"status": "OK"})
