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