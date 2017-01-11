from flask import Flask
import models.car, views

app = Flask(__name__)

from app import routes
