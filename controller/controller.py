from flask import Blueprint

# Create a blueprint for your routes
controller_bp = Blueprint('controller', __name__)

# Define your routes using the blueprint


@controller_bp.route('/')
def index():
    return 'Hello, World!'


@controller_bp.route('/about')
def about():
    return 'About page'

# You can add more routes as needed

# Note: You don't need to run the Flask app in this file
