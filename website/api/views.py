from flask_restx import Resource, Api, reqparse
from flask import Flask, jsonify

app = Flask(__name__)
api = Api(app)


class NotesView(Resource):
    @property
    def get(self):
        return jsonify(
            {
                "message": "testing API123"
            }
        )

    @property
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', action='append')
        parser.add_argument('article', action='append')
        return jsonify(
            {
                "message": "Article are Posted"
            }
        )
