from cProfile import run
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

def select(id):
    make = None

    sql = "SELECT * FROM makes WHERE id = %s"
    values = [id]

    result = run_sql(sql, values)[0]

    if result is not None:
        make = Make(result['name'], result['id'])
    return make

def update(make):
    
    sql = "UPDATE makes SET name = %s WHERE id = %s"
    values = [make.name, make.id]

    run_sql(sql, values)

def delete_all():
    pass

def delete():
    pass