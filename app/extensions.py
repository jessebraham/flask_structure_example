#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

Instantiate any Flask extensions used by our application here. In our case, we
are only using Flask-SQLAlchemy.

Author:     Jesse Braham <jesse@beta7.io>
Created:    May, 2018
Modified:   -

'''

from flask_sqlalchemy import SQLAlchemy


# Flask-SQLAlchemy
# http://flask-sqlalchemy.pocoo.org/latest/
db = SQLAlchemy()
