#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from geekup import app
from geekup.models import db
try:
    from greatape import MailChimp
except ImportError:
    import sys
    print >> sys.stderr, "greatape is not installed. MailChimp support will be disabled."

db.create_all()
app.config['ASSETS_DEBUG'] = True
app.run('0.0.0.0', 4000, debug=True)
