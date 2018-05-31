#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

The main configuration file for our example Flask application.

Author:     Jesse Braham <jesse@beta7.io>
Created:    May, 2018
Modified:   -

'''

import logging
import os


# Store the absolute path to the root of the project directory, which is just
# the parent of the config directory. This is useful for defining the paths to
# the database and log files below.
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir))


# ----------------------------------------------------------------------------
# Flask Application Configuration
# ----------------------------------------------------------------------------

# For more information on configuring the Flask application object, see:
# http://flask.pocoo.org/docs/1.0/config/

# Since we are in development, we will enable debugging. Testing should be set
# to True only when running unit tests, but should be disabled otherwise.
# These values can both be overriden in 'instance/settings.py'.
DEBUG = True
TESTING = False

# Set the secret key to a random string in 'instance/settings.py'
SECRET_KEY = 'a-not-so-secret-key-000-!!!'


# -----------------------------------------------------------------------------
# Logging Configuration
# -----------------------------------------------------------------------------

# For more information on the Python and Flask `logging` modules, see:
# https://docs.python.org/3.6/library/logging.html
# http://flask.pocoo.org/docs/1.0/logging/

# We're using a pretty generic logging format here. Again, these values can be
# overriden in 'instance/settings.py' if you wish.
LOGGING_FORMAT = '%(asctime)s %(levelname)s: %(message)s ' \
                 '[in %(pathname)s:%(lineno)d]'

# Set the location of the log file. We will store it in our 'instance'
# directory for this example, but this can be changed to a more suitable
# location based on your application. If you do not wish to use file logging,
# these configuration values will need to be updated to reflect such.
LOGGING_LOCATION = os.path.join(PROJECT_ROOT, 'instance', 'app.log')

# By default, assume we're debugging our application, so set the log level to
# Debug to ensure we receive all log data. In production this would be
# overriden in 'instance/settings.py'.
LOGGING_LEVEL = logging.DEBUG


# ----------------------------------------------------------------------------
# Flask Extension Configuration
# ----------------------------------------------------------------------------

# For more information on Flask-SQLAlchemy's configuration, see:
# http://flask-sqlalchemy.pocoo.org/2.3/config/

# Define the path to our database for SQLAlchemy. For this example, we're
# using SQLite, so we need to provide a path to the database file. If you are
# using a database such as MySQL, PostgreSQL, etc., the URI will need to point
# to the location of the server, and server credentials will need to be added
# to the configuration.
SQLALCHEMY_DATABASE_URI = 'sqlite:///{root}/{dir}/{filename}'.format(
    root=PROJECT_ROOT, dir='instance', filename='app.db')

# We're not planning on using SQLAlchemy's event system, so we'll disable the
# Track Modifications flag to reduce our application's memory footprint.
SQLALCHEMY_TRACK_MODIFICATIONS = False
