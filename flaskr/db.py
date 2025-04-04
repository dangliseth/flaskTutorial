import mysql.connector

from datetime import datetime

import click
from flask import current_app, g

def get_db():
    """Get a connection to the database. If a connection already exists, return it."""
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['DATABASE']['host'],
            user=current_app.config['DATABASE']['user'],
            password=current_app.config['DATABASE']['password'],
            database=current_app.config['DATABASE']['database']
        )

        g.db.row_factory = mysql.connector.Row
    return g.db

def close_db(e=None):
    """Close the database connection if it exists."""
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)