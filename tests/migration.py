from playhouse.migrate import *
import datetime
import models.calc

my_db = SqliteDatabase('calc.db')
migrator = SqliteMigrator(my_db)

amount_1 = IntegerField(default=0)
amount_2 = IntegerField(default=0)
amount_3 = IntegerField(default=0)

note = TextField(default="")

with my_db.transaction():
    migrate(
        migrator.add_column("Building", 'note', note)
    )

models.calc.initialize()