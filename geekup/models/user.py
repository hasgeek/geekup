# -*- coding: utf-8 -*-
from flask import g
from flaskext.lastuser.sqlalchemy import UserBase
from geekup.models import db


__all__ = ['User']


class User(db.Model, UserBase):

    __tablename__ = 'user'
    #: Events that a user owns
    events = db.relationship('Event', backref='user',
                                lazy='dynamic')

    def __repr__(self):
        return self.fullname


def default_user(context):
    return g.user.id if g.user else None
