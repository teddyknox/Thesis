from shovel import task

@task
def migration_1():
    from playhouse.migrate import *
    from peewee import *
    db = SqliteDatabase('../data/images.db')
    migrator = SqliteMigrator(db)

    model_score = FloatField(null=True)
    generation_method = CharField(default="random")

    with db.transaction():
        migrate(
            migrator.add_column('image', 'model_score', model_score),
            migrator.add_column('image', 'generation_method', generation_method)
        )

    print "Done."
