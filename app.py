from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('FamBam', user='johnrissmiller', password='12345', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Person(BaseModel):
    name = CharField()
    age = IntergerField()
    pets = Charfield()

db.connect()
db.drop_tables([FamBam])
db.create_tables([FamBam])

Person(name='Lenore', age=69).save()
Person(name='Mark', age=69).save()
Person(name='Matthew', age=39).save()
Person(name='Claudia', age=37).save()
Person(name='Timothy', age=36).save()
Person(name='Ashley', age=36).save()
Person(name='Daniel', age=34).save()
Person(name='Renee', age=31).save()
Person(name='Katherine', age=25).save()
Person(name='John', age=27).save()

app = Flask(__name__)