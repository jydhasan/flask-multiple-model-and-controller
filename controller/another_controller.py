from flask import Blueprint

# Create a blueprint for your routes
another_controller_bp = Blueprint('another_controller', __name__)

# Define your routes using the blueprint


@another_controller_bp.route('/another')
def another():
    return 'Another page'

# You can add more routes as needed

# Note: You don't need to run the Flask app in this file
