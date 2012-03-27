#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from geekup.models import *
from flaskext.wtf import (
    Form,
    TextField,
    SelectField,
    QuerySelectField,
    Required,
    Email,
    NoneOf,
    DateField,
    TextAreaField,
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
    ('', u''),
    ('1', u'Twitter'),
    ('2', u'Facebook'),
    ('3', u'LinkedIn'),
    ('5', u'Google Plus'),
    ('4', u'Google/Bing Search'),
    ('10', u'Discussion Group or List'),
    ('6', u'Blog'),
    ('7', u'Email/IM from Friend'),
    ('8', u'Colleague at Work'),
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

def get_speakers():
    return Speaker.query.order_by('name').all()

def get_users():
    return User.query.order_by('fullname').all()

def get_city():
    return City.query.order_by('title').all()

def get_venue():
    return Venue.query.order_by('title').all()

class NewForm(Form):

    name = TextField('Name', validators=[Required('A name is required')])
    title = TextField('Title', validators=[Required('A title is required')])
    date = DateField('Date', validators=[Required('Propose a date')])
    description = TextAreaField('Description', validators=[Required('Describe the Geekup')])
    speaker = QuerySelectField("Speaker", query_factory=get_speakers, get_label='name', allow_blank=True,
        description="Speaker for the Geekup")
    speaker_bio = TextAreaField('Speaker Bio', validators=[Required('Short bio of the speaker')])
    schedule_data = TextAreaField('Schedule')    
    photo = TextField('Photo')
    user_id = QuerySelectField('Select a user', query_factory= get_users, get_label='fullname')
    city_id = QuerySelectField('Select a city', query_factory=get_city, get_label='title')
    venue_id = QuerySelectField('Select a venue', query_factory=get_venue, get_label='title')