from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import app_config

database = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    application = Flask(
        import_name="app",
        template_folder="templates",
        static_folder='static',
        instance_relative_config=True
    )

    application.config.from_object(app_config[config_name])
    database.init_app(application)
    migrate.init_app(application, database, directory="dole_migrations")
    register_blueprints(application)
    return application


def register_blueprints(application):
    # Import all BluePrints
    from .home import home as home_blueprint
    application.register_blueprint(home_blueprint, url_prefix='/home')
