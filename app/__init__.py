from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

# Initialize db and migrate
db = SQLAlchemy()
migrate = Migrate()



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.blueprints.heroes import heroes_bp
    from app.blueprints.powers import powers_bp
    from app.blueprints.hero_powers import hero_powers_bp
    
    app.register_blueprint(heroes_bp, url_prefix='/heroes')
    app.register_blueprint(powers_bp, url_prefix='/powers')
    app.register_blueprint(hero_powers_bp, url_prefix='/hero_powers')
    
    return app
