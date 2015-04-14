from peewee import *
from models import *

db.connect()
db.create_tables([Image])
