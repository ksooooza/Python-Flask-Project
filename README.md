# Python-Flask-Project

This project is an API built using Python, Peewee, and Flask, with full CRUD functionality.

---

### Model:
```
class Person(BaseModel):
    name = CharField()
    age = IntegerField()
    pets = CharField()
```
<br />
---
<br />
### Routes:
<br />
/person/: returns all of the people in the API
<br />
Example of returned content:

```
  {
    "age": 69,
    "id": 1,
    "name": "Lenore",
    "pets": "Belle and Llywellen"
  },
  {
    "age": 69,
    "id": 2,
    "name": "Mark",
    "pets": "Table Saw"
  },
  {
    "age": 39,
    "id": 3,
    "name": "Matthew",
    "pets": "Dexter and Lucy"
  }
 ```
 
<br />
/person/<id>: returns a single person by their ID
<br />
Example of returned content:
<br />
    
```
  {
    "age": 34,
    "id": 7,
    "name": "Daniel",
    "pets": "Tin tin and Kane"
  }
```
<br />
---
<br />
### Future Updates:
<br />
- Creating more than one table/model for the database
- Having a model with a many-to-one or a one-to-many relationship
- Try using web scraping to seed my database
<br />
---
<br />
### Technologies Used:
<br />
- Flask, Peewee, Python
- Routing, Postman, CRUD
