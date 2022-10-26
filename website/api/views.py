from flask_restx import Resource
from flask import jsonify

class NotesView(Resource):
    def get(self):
        return jsonify(
            {
                "message": "testing API",
                "message2": "Testing API 2q"
            }
        )
