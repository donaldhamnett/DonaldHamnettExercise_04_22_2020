from flask import Blueprint

history = Blueprint('history', __name__)

from app.history import views