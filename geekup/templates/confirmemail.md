Hello {{ participant.fullname }},

This is a confirmation email for your registration for "{{ participant.event.title }}".

[Click here to confirm your email address and registration][confirm]

[confirm]: {{ url_for('confirm_email', _external=True, pid=participant.id, key=participant.email_key) }}

[Geekup][gu] is a service of [HasGeek][hg]. Write to us at
info@hasgeek.com if you have suggestions or questions on this service.

[gu]: https://geekup.in
[hg]: https://hasgeek.com

If you did not register, you may safely ignore this email and your registration will be automatically removed.

Regards
The non-sentient HasGeek email robot
