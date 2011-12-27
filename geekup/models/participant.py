# -*- coding: utf-8 -*-

from geekup.models import db, BaseMixin
from datetime import datetime


class Participant(db.Model, BaseMixin):
    """
    Participant data, as submitted from the registration form.
    """
    __tablename__ = 'participant'
    #: User's full name
    fullname = db.Column(db.Unicode(80), nullable=False)
    #: User's email address
    email = db.Column(db.Unicode(80), nullable=False)
    #: User's company name
    company = db.Column(db.Unicode(80), nullable=False)
    #: User's job title
    jobtitle = db.Column(db.Unicode(80), nullable=False)
    #: User's twitter id (optional)
    twitter = db.Column(db.Unicode(80), nullable=True)
    #: How did the user hear about this event?
    referrer = db.Column(db.Integer, nullable=False, default=0)
    #: User category, defined by a reviewer
    category = db.Column(db.Integer, nullable=False, default=0)
    #: User agent with which the user registered
    useragent = db.Column(db.Unicode(250), nullable=True)
    #: Date the user registered
    regdate = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    #: Submitter's IP address, for logging
    #: (45 chars to accommodate an IPv6 address)
    ipaddr = db.Column(db.Text(45), nullable=False)
    #: Has the user's application been approved?
    approved = db.Column(db.Boolean, default=False, nullable=False)
    #: RSVP status codes:
    #: A = Awaiting Response
    #: Y = Yes, Attending
    #: M = Maybe Attending
    #: N = Not Attending
    rsvp = db.Column(db.Integer, default=0, nullable=False)
    #: Did the participant attend the event?
    attended = db.Column(db.Boolean, default=False, nullable=False)
    #: Datetime the participant showed up
    attenddate = db.Column(db.DateTime, nullable=True)
    #: Have we sent this user an email
    email_sent = db.Column(db.Boolean, default=False, nullable=False)
    #: Key created with coaster.secretkey
    email_key = db.Column(db.Unicode(44), nullable=True)
    #: Is it confirmed or not
    email_status = db.Column(db.Boolean, default=False, nullable=False)

    #: Event they'd like to attend
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

    def __repr__(self):
        return self.fullname
