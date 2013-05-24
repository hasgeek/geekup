#!/usr/bin/env python
from geekup import app, init_for
from geekup.models import db

init_for('dev')
db.create_all()
app.run('0.0.0.0', 4000, debug=True)
