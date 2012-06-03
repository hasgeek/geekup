# -*- coding: utf-8 -*-

from geekup.models import db, BaseMixin


class Venue(BaseMixin, db.Model):
    """
    Venue database since we'll want to reuse that.
    """
    __tablename__ = 'venue'
    #: Name of the venue
    name = db.Column(db.Unicode(80), nullable=False)
    #: Display name of the venue
    title = db.Column(db.Unicode(80), nullable=False)
    #: Description for the venue
    description = db.Column(db.Text)
    #: Address of the venue
    address = db.Column(db.Text, nullable=True)
    #: Latitude of the venue
    lat = db.Column(db.Float(10))
    #: Longitude of the venue
    lng = db.Column(db.Float(10))

    #: Events associated with the venue
    events = db.relationship('Event', backref='venue',
                                lazy='dynamic')
    #: City of the venue
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))

    def __repr__(self):
        return self.title
