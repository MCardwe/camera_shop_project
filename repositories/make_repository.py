from cProfile import run
from unicodedata import name
from db.run_sql import run_sql

from models.camera import Camera
from models.make import Make


def save(make):
    
    sql = "INSERT INTO makes (name, active) VALUES (%s, %s) RETURNING *"
    values = [make.name, make.active]

    results = run_sql(sql, values)
    id = results[0]['id']
    make.id = id

    return make

def select_all():
    makes = []

    sql = "SELECT * FROM makes"

    results = run_sql(sql)

    for row in results:
        make = Make(row['name'], row['id'], row['active'])
        makes.append(make)

    return makes

def select(id):
    make = None

    sql = "SELECT * FROM makes WHERE id = %s"
    values = [id]

    result = run_sql(sql, values)[0]

    if result is not None:
        make = Make(result['name'], result['id'], result['active'])
    return make

def update(make):
    
    sql = "UPDATE makes SET (name, active) = (%s, %s) WHERE id = %s"
    values = [make.name, make.active, make.id]

    run_sql(sql, values)

def delete_all():
    
    sql = "DELETE FROM makes"
    run_sql(sql)

def delete(id):
    
    sql = "DELETE FROM makes WHERE id = %s"
    values = [id]

    run_sql(sql, values)