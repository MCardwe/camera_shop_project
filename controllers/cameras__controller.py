from flask import Flask, render_template, redirect, request
from flask import Blueprint

from models.camera import Camera
from models.make import Make

import repositories.camera_repository as camera_repository
import repositories.make_repository as make_repository

cameras_blueprint = Blueprint("cameras", __name__)

@cameras_blueprint.route('/cameras', methods = ['GET'])
def cameras():
    cameras = camera_repository.select_all()
    return render_template('cameras/index.html', cameras=cameras)

@cameras_blueprint.route('/cameras/new', methods=['GET'])
def new_camera():
    makes = make_repository.select_all()
    cameras = camera_repository.select_all()
    return render_template('cameras/new.html', makes=makes, cameras=cameras)

@cameras_blueprint.route("/cameras", methods=['POST'])
def add_camera():
    stock = 0
    stock_count_form = request.form['stock']
    buy_price = 0
    buy_price_form = request.form['buy_price']
    sell_price = 0
    sell_price_form = request.form['sell_price']

    name = request.form['name']
    make_id = request.form['make_id']
    type = request.form['type']
    description = request.form['description']

    if stock_count_form is not None:
        stock = stock_count_form

    if buy_price_form is not None:
        buy_price = buy_price_form

    if sell_price_form is not None:
        sell_price = sell_price_form

    make = make_repository.select(make_id)
    camera = Camera(name, make, type, description, stock, buy_price, sell_price)

    camera_repository.save(camera)
    return redirect('/cameras')


@cameras_blueprint.route("/cameras/<id>", methods=['GET'])
def show(id):
    camera = camera_repository.select(id)
    return render_template('cameras/show.html', camera=camera)