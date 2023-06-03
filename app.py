# from flask import Flask
# from controller.controller import controller_bp
# from controller.another_controller import another_controller_bp

# # Create the Flask application
# app = Flask(__name__)

# # Register the blueprints
# app.register_blueprint(controller_bp)
# app.register_blueprint(another_controller_bp)

# # Run the Flask app
# if __name__ == '__main__':
#     app.run()
from flask import Flask
from model.model import db, User
from model.another_model import AnotherModel
from controller.controller import controller_bp
from controller.another_controller import another_controller_bp

app = Flask(__name__)

# Configure the database URI (SQLite in this example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Register the blueprints
app.register_blueprint(controller_bp)
app.register_blueprint(another_controller_bp)
# Create the database tables
with app.app_context():
    db.create_all()

# Run the Flask app
if __name__ == '__main__':
    app.run()
