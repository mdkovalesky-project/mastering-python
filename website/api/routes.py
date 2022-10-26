from flask import Blueprint
from flask_restx import Api

from .views import NotesView


api_blueprint = Blueprint("api", __name__)

api = Api(api_blueprint)

api.add_resource(NotesView, "/notes")