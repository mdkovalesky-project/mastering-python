from flask import Blueprint
from flask_restx import Api

from .views import NotesView

api_blueprint = Blueprint("api", __name__, url_prefix="/api/v1/")

api = Api(
    api_blueprint,
    version="1.0",
    title="Nodium",
    description="Article",
    
) # <- Konfigurasi API untuk memberikan title dan description
# It's a way to group your routes.
# ns = api.namespace("notes", desciption="Notes operations")
# api.add_namespace(ns, NotesView)

api.add_resource(NotesView, "/notes") # <- ini routes notes

