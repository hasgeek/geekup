# -*- coding: utf-8 -*-

from geekup.models import db, BaseNameMixin

__all__ = ['City']

class City(db.Model, BaseNameMixin):
    """
    A city, mostly for feeds and subscription
    """
    __tablename__ = 'city'
    #: All the venues in a city
    venues = db.relationship('Venue', backref='city',
                                lazy='dynamic')
    #: All events in a city
    # events = db.relationship('Event', backref='city',
    #                             lazy='dynamic')

    def __repr__(self):
        return self.title
