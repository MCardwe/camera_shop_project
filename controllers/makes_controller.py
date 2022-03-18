from flask import Flask, render_template, redirect, request
from flask import Blueprint

from models.camera import Camera
from models.make import Make

import repositories.camera_repository as camera_repository
import repositories.make_repository as make_repository

makes_blueprint = Blueprint("makes", __name__)