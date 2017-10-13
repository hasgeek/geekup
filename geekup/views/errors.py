#!/usr/bin/env python
# -*- coding: utf8 -*-

from geekup import app

from flask import render_template

@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html.jinja2'), 404
