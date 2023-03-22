from . import db
from peewee import * 

# base model def
class BaseModel(Model):
    class Meta:
        database = db
