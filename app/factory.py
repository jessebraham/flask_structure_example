#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

Define the factory function for our Flask application. Performs configuration
from our settings file, and optionally from the instance settings if provided.

Author:     Jesse Braham <jesse@beta7.io>
Created:    May, 2018
Modified:   -

'''

import logging

from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from app.blueprints import home_bp
from app.errors import error_templates
from app.extensions import db


def create_app(settings_override=None):
    '''
    Create a Flask application using the app factory pattern.
    (See http://flask.pocoo.org/snippets/20/)

    Load the default configuration from the 'config/settings.py' file, and
    optionally load the configuration from 'instance/settings.py', if present.

    :param settings_override: Override settings
    :return:                  Flask appplication instance
    '''

    # Create the Flask application object. The 'instance_relative_config'
    # parameter tells the app that configuration files are relative to the
    # instance directory.
    app = Flask(__name__, instance_relative_config=True)

    # Tell our application to load its configuration from config.settings, and
    # attempt to load any additional settings from the 'settings.py' file
    # located in the instance directory.
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    # Configure the application's file logger and register any middleware.
    logger(app)
    middleware(app)

    # Create handlers for all necessary HTTP errors. In our case, we're simply
    # rendering templates for each error of interest.
    error_templates(app)

    # Register all required Blueprints with our Flask application.
    app.register_blueprint(home_bp)

    # Configure and register all required extensions with our Flask
    # application.
    extensions(app)

    # Return the fully configured Flask application object.
    return app


def logger(app):
    '''
    Configure a file handler for use with the Flask application's built-in
    logger. The log location, log level, and log formats can all be configured
    via the config file. Note that this function mutates the provided 'app'
    parameter.

    :param app: Flask application instance
    '''

    # Instantiate a new File Handler, storing our log files in the directory
    # specified by the app config. Set the log level to the configured value.
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])

    # Create a log formatter, using the format specified in the app config.
    # Apply this formatter to the above created handler.
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)

    # Register our handler with the Flask object's pre-configured logger
    # object.
    app.logger.addHandler(handler)


def middleware(app):
    '''
    Register 0 or more middleware. Note that this function mutates the
    provided 'app' parameter.

    :param app: Flask application instance
    '''

    # Swap request.remote_addr with the real IP address even if behind a
    # proxy.
    #
    # http://werkzeug.pocoo.org/docs/0.14/contrib/fixers/#werkzeug.contrib.fixers.ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)


def extensions(app):
    '''
    Register 0 or more extensions with the Flask application object. Note that
    this function mutates the provided 'app' parameter.

    :param app: Flask application instance
    '''

    # Register the SQLAlchemy database object with our Flask application.
    db.init_app(app)
