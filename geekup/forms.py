#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from flask.ext.wtf import (
    Form,
    TextField,
    SelectField,
    Required,
    Email,
    NoneOf,
    )


USER_CATEGORIES = [
    ('0', u'Unclassified'),
    ('1', u'Student or Trainee'),
    ('2', u'Developer'),
    ('3', u'Designer'),
    ('4', u'Manager, Senior Developer/Designer'),
    ('5', u'CTO, CIO, CEO'),
    ('6', u'Entrepreneur'),
    ]


REFERRERS = [
    ('0', u''),
    ('1', u'Twitter'),
    ('2', u'Facebook'),
    ('3', u'LinkedIn'),
    ('5', u'Google Plus'),
    ('4', u'Google/Bing Search'),
    ('10', u'Discussion Group or List'),
    ('6', u'Blog'),
    ('7', u'Email/IM from Friend'),
    ('8', u'Colleague at Work'),
    ('11', u'IRC'),
    ('9', u'Other'),
    ]


GALLERY_SECTIONS = [
    (u'Basics', u'basics'),
    (u'Business', u'biz'),
    (u'Accessibility', u'accessibility'),
    (u'Typography', u'typography'),
    (u'CSS3', u'css'),
    (u'Audio', u'audio'),
    (u'Video', u'video'),
    (u'Canvas', u'canvas'),
    (u'Vector Graphics', u'svg'),
    (u'Geolocation', u'geolocation'),
    (u'Mobile', u'mobile'),
    (u'Websockets', u'websockets'),
    (u'Toolkits', u'toolkit'),
    (u'Showcase', u'showcase'),
    ]


RSVP_STATUS = [
    (u'0', u''),
    (u'1', u'Yes, Attending'),
    (u'2', u'Maybe Attending'),
    (u'3', u'Not Attending'),
    ]


class RegisterForm(Form):
    fullname = TextField('Full name',
                         validators=[Required("Your name is required")])
    email = TextField('Email address',
                      validators=[Required("Your email address is required"),
                      Email()])
    company = TextField('Company name')
    jobtitle = TextField('Job title')
    twitter = TextField('Twitter id')
    referrer = SelectField('How did you hear about this event?',
                           choices=REFERRERS)


class RsvpForm(Form):
    rsvp = SelectField('Are you attending this event?',
                       choices=RSVP_STATUS,
                       validators=[NoneOf(u'0', 'Please indicate your RSVP status')])
