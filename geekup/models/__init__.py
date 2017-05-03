from flask_sqlalchemy import SQLAlchemy
from geekup import app
from coaster.sqlalchemy import BaseMixin, BaseNameMixin

db = SQLAlchemy(app)

from geekup.models.city import *
from geekup.models.event import *
from geekup.models.participant import *
from geekup.models.speaker import *
from geekup.models.sponsor import *
from geekup.models.user import *
from geekup.models.venue import *
