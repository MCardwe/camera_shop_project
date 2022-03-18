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