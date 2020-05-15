from flask import Blueprint

update = Blueprint('update', __name__)

from app.update import views