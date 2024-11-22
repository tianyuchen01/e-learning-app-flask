from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    # Creating new App
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Simple Secret Key'

    # Adding database to the application
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Adding routes
    from .routes import routes
    app.register_blueprint(routes, url_prefix='/')

    create_database(app)
    return app

def create_database(app):
    with app.app_context():
        db.create_all()
