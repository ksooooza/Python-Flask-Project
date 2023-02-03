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