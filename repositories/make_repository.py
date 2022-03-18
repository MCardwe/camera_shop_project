from unicodedata import name
from db.run_sql import run_sql

from models.camera import Camera
from models.make import Make


def save(make):
    
    sql = "INSERT INTO makes (name) VALUES (%s) RETURNING *"
    values = [make.name]

    results = run_sql(sql, values)
    id = results[0]['id']
    make.id = id

    return make

def select_all():
    makes = []

    sql = "SELECT * FROM makes"

    results = run_sql(sql)

    for row in results:
        make = Make(row['name'], row['id'])
        makes.append(make)

    return makes

def select():
    pass

def update():
    pass

def delete_all():
    pass

def delete():
    pass