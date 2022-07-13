from flask import Flask, request
from flask_restx import Api, Resource
from pprint import pprint

PUT = {
    "author": "Not me",
    "text": "New Note"
}

PATCH = {"text": "Note, that newer then last one"}

app = Flask(__name__)
app. config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 2}

api = Api(app)
note_ns = api.namespace('notes')

notes = {
    1: {
        "id": 1,
        "text": "this is my super secret note",
        "author": "me"
    },
    2: {
        "id": 2,
        "text": "oh, my note",
        "author": "me"
    }
}


@note_ns.route('/<int:uid>')
class NoteView(Resource):
    def put(self, uid):
        if uid not in notes:
            return "", 404
        note = notes[uid]

        req_json = request.json
        note["text"] = req_json.get("text")
        note["author"] = req_json.get("author")

        notes[uid] = note
        return "", 204

    def patch(self, uid):
        if uid not in notes:
            return "", 404

        note = notes[uid]
        req_json = request.json
        if "text" in req_json:
            note["text"] = req_json.get("text")
        if "author" in req_json:
            note["author"] = req_json.get("author")

        notes[uid] = note
        return "", 204

    def delete(self, uid):
        if uid not in notes:
            return "", 404
        del notes[uid]
        return "", 204


if __name__ == '__main__':
    client = app.test_client()
    # response = client.put('/notes/1', json=PUT)
    # response = client.patch('/notes/1', json=PATCH)
    # response = client.delete('/notes/1')
    pprint(notes, indent=2)
