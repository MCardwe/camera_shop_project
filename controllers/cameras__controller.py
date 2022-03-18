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
    return render_template('cameras/new.html', makes=makes)