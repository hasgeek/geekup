#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from geekup import app
from geekup.models import db
from os import environ

environ['GEEKUP_ENV'] = 'dev'

db.create_all()
app.config['ASSETS_DEBUG'] = True
app.run('0.0.0.0', 4000, debug=True)
