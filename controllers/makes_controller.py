from flask import Flask, render_template, redirect, request
from flask import Blueprint

from models.camera import Camera
from models.make import Make

import repositories.camera_repository as camera_repository
import repositories.make_repository as make_repository

makes_blueprint = Blueprint("makes", __name__)

@makes_blueprint.route("/makes", methods=["GET"])
def makes():
    makes = make_repository.select_all()
    return render_template("makes/index.html", makes=makes)

@makes_blueprint.route("/makes/new", methods=["GET"])
def new_form():
    return render_template("makes/new.html")

@makes_blueprint.route("/makes", methods=["POST"])
def add():
    name = request.form['name']
    make = Make(name)
    make_repository.save(make)
    return redirect("/makes")

@makes_blueprint.route("/makes/<id>/edit", methods=["GET"])
def edit_form(id):
    make = make_repository.select(id)
    return render_template("makes/edit.html", make=make)

@makes_blueprint.route("/makes/<id>/edit", methods=["POST"])
def edit(id):
    name = request.form['name']
    make = Make(name, id)
    make_repository.update(make)
    return redirect("/makes")

@makes_blueprint.route("/makes/<id>/delete")
def delete(id):
    make_repository.delete(id)
    return redirect("/makes")

@makes_blueprint.route("/makes/<id>")
def show(id):
    all_cameras = camera_repository.select_all()
    make = make_repository.select(id)
    cameras_list = []
    no_cameras = False
    for camera in all_cameras:
        if camera.make.id == make.id:
            cameras_list.append(camera)

    if len(cameras_list) == 0:
        no_cameras = True
        
    return render_template("/makes/show.html", cameras=cameras_list, make=make, no_cameras=no_cameras)