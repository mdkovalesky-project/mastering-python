from flask_restx import Resource, reqparse
from flask import jsonify

from website.api.schema import note_schema, note_schemas
from website.models import Note, User

class NotesView(Resource):
    def get(self):
        notes = Note.query.all()
        return note_schemas.dump(notes)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', action='append')
        parser.add_argument('article', action='append')
        return jsonify(
            {
                "message": "Article are Posted"
            }
        )
