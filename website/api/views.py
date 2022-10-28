from flask_restx import Resource, Api, reqparse
from flask import Flask, jsonify

app = Flask(__name__)
api = Api(app, title='Nodium', description='Start from Reader Become Writer')


class NotesView(Resource):
    def get(self):
        return jsonify(
            {
                "message": "testing API123",
                "message2": "Testing API 2"
            }
        )

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', action='append')
        parser.add_argument('article', action='append')
