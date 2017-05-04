#!/usr/bin/env python
import sys
from geekup import app
from geekup.models import db

db.create_all()
try:
    port = int(sys.argv[1])
except (IndexError, ValueError):
    port = 4000
app.run('0.0.0.0', port)
