from flask import Flask, request
from flask_restx import Api, Resource
from pprint import pprint

app = Flask(__name__)
app. config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 2}

INSTANCE = {
    "id": 4,
    "text": "Текст заметки идет здесь",
    "author": "Кто ты?"
}

api = Api(app)
note_ns = api.namespace('notes')

notes = [
    {
        "id": 1,
        "text": "This is my note!",
        "author": "me",
    },
    {
        "id": 2,
        "text": "This is also my note!",
        "author": "me",
    }
]


@note_ns.route('/')
class NotesView(Resource):
    def post(self):
        req_json = request.json
        notes.append(req_json)
        return "", 201


if __name__ == '__main__':
    client = app.test_client()
    response = client.post('/notes/', json=INSTANCE)
    pprint(notes, indent=2)
