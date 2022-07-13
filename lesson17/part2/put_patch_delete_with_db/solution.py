from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from prettytable import prettytable

PUT = {
    "author": "Not me",
    "text": "New Note"
}

PATCH = {"text": "Note, that newer then last one"}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app. config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 2}
db = SQLAlchemy(app)

api = Api(app)
note_ns = api.namespace('notes')


class Note(db.Model):
    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    author = db.Column(db.String)


class NoteSchema(Schema):
    id = fields.Int(dump_only=True)
    text = fields.Str()
    author = fields.Str()


note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)

n1 = Note(id=1, text="Моя заметка!", author="me")
n2 = Note(id=2, text="Это тоже моя заметка", author="me")

db.drop_all()
db.create_all()

with db.session.begin():
    db.session.add_all([n1, n2])


@note_ns.route('/<int:uid>')
class NoteView(Resource):
    def put(self, uid: int):
        note = Note.query.get(uid)
        if not note:
            return "", 404
        req_json = request.json
        note.text = req_json.get("text")
        note.author = req_json.get("author")
        db.session.add(note)
        db.session.commit()
        return "", 204

    def patch(self, uid: int):
        note = Note.query.get(uid)
        if not note:
            return "", 404
        req_json = request.json
        if "text" in req_json:
            note.text = req_json.get("text")
        if "author" in req_json:
            note.author = req_json.get("author")
        db.session.add(note)
        db.session.commit()
        return "", 204

    def delete(self, uid: int):
        note = Note.query.get(uid)
        if not note:
            return "", 404
        db.session.delete(note)
        db.session.commit()
        return "", 204


# # # # # # # # # # # #
if __name__ == '__main__':
    client = app.test_client()                          # TODO вы можете раскомментировать
    # response = client.put('/notes/1', json=PUT)       # соответсвующе функции и
    # response = client.patch('/notes/1', json=PATCH)   # воспользоваться ими для самопроверки
    # response = client.delete('/notes/1', json='')     # аналогично заданию `post_with_db`
    session = db.session()
    cursor = session.execute("SELECT * FROM note").cursor
    mytable = prettytable.from_db_cursor(cursor)
    mytable.max_width = 30
    print("БАЗА ДАННЫХ")
    print(mytable)
