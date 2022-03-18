from db.run_sql import run_sql

from models.camera import Camera
from models.make import Make

import repositories.make_repository as make_repository

def save(camera):
    
    sql = "INSERT INTO cameras (name, make_id, type, description, stock, buy_price, sell_price) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [camera.name, camera.make.id, camera.type, camera.description, camera.stock, camera.buy_price, camera.sell_price]

    results = run_sql(sql, values)
    id = results[0]['id']
    camera.id = id

    return camera

def select_all():
    cameras = []

    sql = "SELECT * FROM cameras"

    results = run_sql(sql)

    for row in results:
        make = make_repository.select(row['make_id'])
        camera = Camera(row['name'], make, row['type'], row['description'], row['stock'], row['buy_price'], row['sell_price'], row['id'])
        cameras.append(camera)
    
    return cameras

def select(id):
    camera = None

    sql = "SELECT * FROM cameras WHERE id = %s"
    values = [id]

    result = run_sql(sql, values)[0]

    if result is not None:
        make = make_repository.select(result['make_id'])
        camera = Camera(result['name'], make, result['type'], result['description'], result['stock'], result['buy_price'], result['sell_price'], result['id'])
    return camera

def update(camera):
    
    sql = "UPDATE cameras SET (name, make_id, type, description, stock, buy_price, sell_price) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [camera.name, camera.make.id, camera.type, camera.description, camera.stock, camera.buy_price, camera.sell_price, camera.id]

    run_sql(sql, values)

def delete_all():
    
    sql = "DELETE FROM cameras"
    run_sql(sql)

def delete(id):
    
    sql = "DELETE FROM cameras WHERE id = %s"
    values = [id]

    run_sql(sql, values)