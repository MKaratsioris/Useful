import os
import logging
from logging.handlers import RotatingFileHandler
import sqlite3
from flask import Flask, g, jsonify
from flasgger import Swagger

from app.db.employee_database import EmployeeDatabase
from app.api.routes import bp as api_bp

DATABASE = "employees.db"


def get_db():
    """
    Opens a new database connection if there is none yet for the current request.
    """
    if 'db' not in g:
        g.db_conn = sqlite3.connect(DATABASE, check_same_thread=False)
        g.db = EmployeeDatabase(g.db_conn)
    return g.db


def close_db(e=None):
    """
    Closes the database connection at the end of the request.
    """
    db_conn = g.pop('db_conn', None)
    if db_conn is not None:
        db_conn.close()


def create_app():
    app = Flask(__name__)

    # Register Blueprint
    app.register_blueprint(api_bp)

    # Teardown DB after request
    app.teardown_appcontext(close_db)

    # Make get_db accessible in routes
    app.get_db = get_db

    # Setup Logging
    log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, 'app.log')

    file_handler = RotatingFileHandler(log_path, maxBytes=10240, backupCount=3)
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    )
    file_handler.setFormatter(file_formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)

    app.logger.info("Flask app created and logging configured")
    
    # Enable Swagger
    Swagger(app)

    # Register custom error handlers
    register_error_handlers(app)

    return app


def register_error_handlers(app):
    """
    Registers custom error handlers for common HTTP errors.
    """

    @app.errorhandler(400)
    def bad_request(error):
        app.logger.warning(f"400 Bad Request: {error}")
        return jsonify({"error": "Bad Request"}), 400

    @app.errorhandler(404)
    def not_found(error):
        app.logger.warning(f"404 Not Found: {error}")
        return jsonify({"error": "Not Found"}), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        app.logger.error(f"500 Internal Server Error: {error}")
        return jsonify({"error": "Internal Server Error"}), 500
