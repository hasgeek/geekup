# -*- coding: utf-8 -*-

from geekup.models import db, BaseMixin


class Sponsor(db.Model, BaseMixin):
    """
    Sponsor data to display on event pages
    """
    __tablename__ = 'sponsor'
    #: Name of the sponsor
    name = db.Column(db.Unicode(80), nullable=False)
    #: Title of the sponsor
    title = db.Column(db.Unicode(80), nullable=False)
    #: Sponsor's logo
    photo = db.Column(db.Unicode(255), nullable=True)
    #: URL to the sponsor's website
    url = db.Column(db.Unicode(255), nullable=True)
    #: Description of sponsor
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return self.title
