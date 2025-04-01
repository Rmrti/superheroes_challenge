from flask import Flask
from flask_migrate import Migrate
from app.models import db  # Import db from models.py
from app.routes import * 

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)  # Use the db from models.py
    migrate.init_app(app, db)

    return app
