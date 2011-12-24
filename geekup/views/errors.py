#!/usr/bin/env python
# -*- coding: utf8 -*-

from geekup import app

from flask import render_template

@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html'), 404


@app.errorhandler(403)
def not_authorized(e):
        return render_template('403.html'), 403
