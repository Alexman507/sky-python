from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from prettytable import prettytable

INSTANCE = {
    "id": 4,
    "text": "Текст заметки идет здесь",
    "author": "Кто ты?"
}

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

db.create_all()

with db.session.begin():
    db.session.add_all([n1, n2])


@note_ns.route('/')
class NotesView(Resource):
    def post(self):
        req_json = request.json
        new_note = Note(**req_json)
        with db.session.begin():
            db.session.add(new_note)
        return "", 201


if __name__ == '__main__':
    client = app.test_client()
    response = client.post('/notes/', json=INSTANCE)
    session = db.session()
    cursor = session.execute("SELECT * FROM note").cursor
    mytable = prettytable.from_db_cursor(cursor)
    mytable.max_width = 30
    print("БАЗА ДАННЫХ")
    print(mytable)
