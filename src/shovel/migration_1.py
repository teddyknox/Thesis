from playhouse.migrate import *
from peewee import *

db = SqliteDatabase('../data/images.db')
migrator = SqliteMigrator(db)

model_score = FloatField(null=True)

with db.transaction():
    migrate(migrator.add_column('image', 'model_score', model_score)

print "Done."
