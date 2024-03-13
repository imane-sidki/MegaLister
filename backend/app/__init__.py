from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://imane:246@localhost/usernames_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()  # Create sql tables for our data models
        
        # Register a custom command
        @app.cli.command("load-usernames") # run 'flask load-usernames' only once before running flask app
        def load_usernames():
            filepath = os.path.join(os.path.dirname(__file__), 'usernames.txt')
            from .utils import load_usernames_bulk  # called here to avoid circular dependency of 'db'
            load_usernames_bulk(filepath)
            print("Usernames loaded successfully.")

    return app
