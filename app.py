from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('fambam', user='johnrissmiller', password='12345', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Person(BaseModel):
    name = CharField()
    age = IntegerField()
    pets = CharField()

db.connect()
db.drop_tables([Person])
db.create_tables([Person])

Person(name='Lenore', age=69, pets="Belle and Llywellen").save()
Person(name='Mark', age=69, pets="Table Saw").save()
Person(name='Matthew', age=39, pets="Dexter and Lucy").save()
Person(name='Claudia', age=37, pets="Raisin(RIP) and Ollie").save()
Person(name='Timothy', age=36, pets="Marley").save()
Person(name='Ashley', age=36, pets="Rigby and Chewie").save()
Person(name='Daniel', age=34, pets="Tin tin and Kane").save()
Person(name='Renee', age=31, pets="Mabel(RIP), Velma Jane, and Etta").save()
Person(name='Katherine', age=25, pets="All the cats").save()
Person(name='John', age=27, pets="Mollie(RIP)").save()

app = Flask(__name__)

@app.route('/person/', methods=['GET', 'POST'])
@app.route('/person/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Person.get(Person.id == id)))
        else:
            people_list = []
            for person in Person.select():
                people_list.append(model_to_dict(person))
            return jsonify(people_list)

    if request.method == 'PUT':
        body = request.get_json()
        Person.update(body).where(Person.id == id).execute()
        return "Person " + str(id) + " has been updated."

    if request.method == 'POST':
        new_person = dict_to_model(Person, request.get_json())
        new_person.save()
        return jsonify({"success": True})

    if request.method == 'DELETE':
        Person.delete().where(Person.id == id).execute()
        return "Person " + str(id) + " deleted."

app.run(debug=True, port=2000)