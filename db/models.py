from peewee import *

# explicit connect management implemented
database = PostgresqlDatabase(None)
# models
class BaseModel(Model):
    class Meta:
        database = database

class Profile(BaseModel):
    username = CharField(max_length=12)

class Manga(BaseModel):
    name = CharField()
    latest_chapter = CharField(null=True)
    subscribers = ManyToManyField(Profile, backref="mangas")

ProfileManga = Manga.subscribers.get_through_model()

# helper that must be run at setup time only
def create_tables():
    with database:
        database.create_tables([Profile, Manga, ProfileManga])