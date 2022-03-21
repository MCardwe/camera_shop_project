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
    stock = request.form['stock']
    buy_price = request.form['buy_price']
    sell_price = request.form['sell_price']

    name = request.form['name']
    make_id = request.form['make_id']
    type = request.form['type']
    description = request.form['description']

    make = make_repository.select(make_id)
    camera = Camera(name, make, type, description, stock, buy_price, sell_price)

    camera_repository.save(camera)
    return redirect('/cameras')


@cameras_blueprint.route("/cameras/<id>", methods=['GET'])
def show(id):
    camera = camera_repository.select(id)
    return render_template('cameras/show.html', camera=camera)

@cameras_blueprint.route("/cameras/<id>/delete", methods=["POST"])
def delete_camera(id):
    camera_repository.delete(id)
    return redirect('/cameras')

@cameras_blueprint.route("/cameras/<id>/edit", methods=["GET"])
def edit_form(id):
    camera = camera_repository.select(id)
    all_cameras = camera_repository.select_all()
    makes = make_repository.select_all()
    return render_template("/cameras/edit.html", camera=camera, makes=makes, all_cameras = all_cameras)

@cameras_blueprint.route("/cameras/<id>/edit", methods=["POST"])
def edit_camera(id):
    camera_to_update = camera_repository.select(id)
    name = request.form['name']
    make_id = request.form['make_id']
    type =  camera_to_update.type
    description = request.form['description']
    stock= request.form['stock']
    buy_price = request.form['buy_price']
    sell_price = request.form['sell_price']
    
    make = make_repository.select(make_id)
    camera = Camera(name, make, type, description, stock, buy_price, sell_price, id)
    camera_repository.update(camera)

    return redirect('/cameras')