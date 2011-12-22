# -*- coding: utf-8 -*-
from geekup.models import db, BaseMixin


class Speaker(db.Model, BaseMixin):
    """
    Speaker data to display on event pages
    """
    __tablename__ = 'speaker'
    #: Name of the speaker
    name = db.Column(db.Unicode(80), nullable=False)
    #: Display name of the speaker
    title = db.Column(db.Unicode(80), nullable=False)
    #: Photo of the speaker
    photo = db.Column(db.Unicode(255), nullable=True)
    #: Generic bio for the speaker
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return self.title
