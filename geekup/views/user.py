#!/usr/bin/env python
# -*- coding: utf8 -*-

from datetime import date
from geekup import app, mail
from geekup.models import *
from geekup.forms import RegisterForm, RsvpForm, RSVP_STATUS
from geekup.views.login import lastuser

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    Markup,
    )
from flask.ext.mail import Message

import json
from markdown import markdown
from uuid import uuid4


@app.route('/')
def index():
    event = Event.query.filter(Event.date >= date.today()).order_by('date').limit(1).first()
    if event is None:
        # No upcoming events. Find most recent past event
        event = Event.query.order_by('date desc').limit(1).first_or_404()
    return redirect(url_for('eventpage', year=event.year, eventname=event.name), 302)


@app.route('/<year>/<eventname>')
def eventpage(year, eventname, regform=None):
    if regform is None:
        regform = RegisterForm()
    event = Event.query.filter_by(name=eventname, year=year).first_or_404()
    try:
        schedule_data = json.loads(event.schedule_data)
    except:
        schedule_data = None
    context = {
            'event': event,
            'schedule_data': schedule_data,
            'regform': regform,
            'event_date': event.date.strftime('%A, %d %B %Y'),
            'speaker_bio': Markup(event.speaker_bio),
            'event_description': Markup(event.description),
            'venue_description': Markup(event.venue.description),
            'venue_address': Markup(event.venue.address),
            }
    return render_template('event.html', **context)


@app.route('/<year>/<eventname>', methods=['POST'])
def register(year, eventname):
    form = RegisterForm()
    event = Event.query.filter_by(name=eventname, year=year).first()
    if form.validate_on_submit():
        participant = Participant()
        form.populate_obj(participant)
        participant.event_id = event.id
        participant.ipaddr = request.environ['REMOTE_ADDR']
        participant.useragent = request.user_agent.string
        participant.email_key = uuid4().hex
        db.session.add(participant)
        db.session.commit()
        if not participant.email_sent:
            msg = Message(subject="Geekup Confirmation",
                          recipients=[participant.email])
            msg.body = render_template("confirmemail.md",
                                       participant=participant)
            msg.html = markdown(msg.body)
            mail.send(msg)
            participant.email_sent = True
            db.session.commit()
        return render_template('regsuccess.html')
    else:
        if request.is_xhr:
            return render_template('regform.html',
                                   regform=form, ajax_re_register=True)
        else:
            flash("Please check your details and try again.", 'error')
            return eventpage(eventname, regform=form)


@app.route('/confirm/<pid>/<key>')
def confirm_email(pid, key, rsvpform=None):
    if rsvpform is None:
        rsvpform = RsvpForm()
    participant = Participant.query.get(pid)
    if participant is not None and participant.email_key == key:
        participant.email_status = True
        db.session.commit()
        tweet = ("I'm attending the #geekup with %s at %s." %
            (participant.event.speaker,
            participant.event.venue.title))
        context = {
            'participant': participant,
            'rsvpform': rsvpform,
            'tweet': tweet,
        }
        return render_template('confirm.html', **context)
    return redirect(url_for('index'))


@app.route('/confirm/<pid>/<key>', methods=['POST'])
def rsvp(pid, key):
    form = RsvpForm()
    participant = Participant.query.get(pid)
    if participant is not None and participant.email_key == key:
        if form.validate_on_submit():
            participant.rsvp = form.data['rsvp']
            db.session.commit()
            return render_template('rsvpsuccess.html')
        else:
            if request.is_xhr:
                context = {
                    'rsvpform': form,
                    'participant': participant,
                     'ajax_re_register': True,
                }
                return render_template('rsvpform.html', **context)
            else:
                flash("Please check your details and try again.", 'error')
                return confirm_email(pid, key, rsvpform=form)
    else:
        return redirect(url_for('index'))


@app.route('/<year>/<eventname>/participants')
@lastuser.requires_permission('siteadmin')
def participant_list(year, eventname):
    event = Event.query.filter_by(name=eventname, year=year).first_or_404()
    participants = Participant.query.filter_by(event=event). \
            order_by('rsvp').all()
    context = {
        'event': event,
        'rsvp': RSVP_STATUS,
        'participants': participants,
    }
    return render_template('participants.html', **context)
