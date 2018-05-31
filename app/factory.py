#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

Define the factory function for our Flask application. Performs configuration
from our settings file, and optionally from the instance settings if provided.

Author:     Jesse Braham <jesse@beta7.io>
Created:    May, 2018
Modified:   -

'''

from flask import Flask


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

    # Return the fully configured Flask application object.
    return app
