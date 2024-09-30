from flask import Flask
from .routes import main  # Import your routes blueprint


def create_app():
    app = Flask(__name__) 
    
    app.register_blueprint(main)

    return app
