import sys
import os.path
from os import environ

environ['GEEKUP_ENV'] = 'prod'
sys.path.insert(0, os.path.dirname(__file__))
from geekup import app as application
