#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

Author:     Jesse Braham <jesse@beta7.io>
Created:    May, 2018
Modified:   -

'''

from flask import Blueprint


# Create the Home Blueprint, setting it to pull templates from the templates
# directory in the blueprint's module, rather than the application-default
# location.
home_bp = Blueprint('home', __name__, template_folder='templates')


@home_bp.route('/')
def index():
    return 'Hello, world!'
