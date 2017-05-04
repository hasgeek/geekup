#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Website server for geekup.in
"""

from flask import Flask
from flask_mail import Mail
from flask_lastuser import Lastuser
from flask_lastuser.sqlalchemy import UserManager
import coaster.app
from baseframe import baseframe, assets, Version
from ._version import __version__

# First, make an app

version = Version(__version__)
app = Flask(__name__, instance_relative_config=True)
lastuser = Lastuser()
mail = Mail()

# Second, setup assets

assets['geekup.js'][version] = 'js/scripts.js'
assets['geekup.css'][version] = 'css/screen.css'

# Third, import the models and views

from . import models, views

# Fourth, setup admin for the models

from flask_admin import Admin
from flask_admin.contrib.sqlamodel import ModelView


class AuthModelView(ModelView):
    def is_accessible(self):
        return lastuser.has_permission('siteadmin')


admin = Admin(app, name='Geekup')
admin.add_view(AuthModelView(models.City, models.db.session))
admin.add_view(AuthModelView(models.Event, models.db.session))
admin.add_view(AuthModelView(models.Participant, models.db.session))
admin.add_view(AuthModelView(models.Speaker, models.db.session))
admin.add_view(AuthModelView(models.Sponsor, models.db.session))
admin.add_view(AuthModelView(models.User, models.db.session))
admin.add_view(AuthModelView(models.Venue, models.db.session))


coaster.app.init_app(app)
baseframe.init_app(app, requires=['jquery.form', 'baseframe-networkbar', 'geekup'])
lastuser.init_app(app)
lastuser.init_usermanager(UserManager(models.db, models.User))
mail.init_app(app)
