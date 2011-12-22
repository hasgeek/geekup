# -*- coding: utf-8 -*-

from geekup.models import db, BaseMixin

from datetime import date

event_speaker = db.Table('event_speaker',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('speaker_id', db.Integer, db.ForeignKey('speaker.id')))

event_sponsor = db.Table('event_sponsor',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('sponsor_id', db.Integer, db.ForeignKey('sponsor.id')))


class Event(db.Model, BaseMixin):
    """
    Events - the core of geekup
    """
    __tablename__ = 'event'
    #: Name of the event
    name = db.Column(db.Unicode(80), nullable=False)
    #: Title of the event
    title = db.Column(db.Unicode(80), nullable=False)
    #: Year of the event
    year = db.Column(db.Integer, default=date.today().year, nullable=False)
    #: Date of the event
    date = db.Column(db.DateTime, nullable=False)
    #: Description for the event
    description = db.Column(db.Text, nullable=False)
    #: Speaker Bio customized for the event
    speaker_bio = db.Column(db.Text, nullable=False)
    #: Schedule JSON for the event.
    schedule_data = db.Column(db.Text, nullable=False)
    #: Photo of the speaker
    photo = db.Column(db.Unicode(255), nullable=True)
    #: Statu of the event:
    #: True = Open
    #: False = Closed
    status = db.Column(db.Boolean, default=True, nullable=False)

    #: Venue for the event, event.venue will give access to the
    #: event's venue object
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
    #: User creating the event, event.user will give access to
    #: the user's object
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #: City for the event, event.city will give access to the
    #: city's object.
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))

    #: List of speakers for the event, event.speakers gives access
    #: to the objects
    speakers = db.relationship('Speaker', secondary=event_speaker,
        backref=db.backref('events', lazy='dynamic'))
    #: List of sponsors for the event, event.sponsors gives access
    #: to the objects
    sponsors = db.relationship('Sponsor', secondary=event_sponsor,
        backref=db.backref('events', lazy='dynamic'))
    #: List of participants, event.participants gives access to
    #: the objects
    participants = db.relationship('Participant', backref='event',
                                lazy='dynamic')

    def __repr__(self):
        return self.title
