# У вас настроенный фласк, модель,
# пара записей в бд и схема для сериализации.
#
# Вам необходимо:
#
# 1. Cоздать Class Based View, который позволяет
#    с помощью GET-запроса на адрес `/notes`
#    получить список всех сущностей.
#
# 2. Создать Class Based View, который позволяет
#    с помощью GET-запроса на адрес `/notes/{id}`
#    получить сущность с соответствующим id

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app. config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 2}
db = SQLAlchemy(app)


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

api = Api(app)
note_ns = api.namespace('notes')

n1 = Note(id=1, text="Моя заметка!", author="me")
n2 = Note(id=2, text="Это тоже моя заметка", author="me")

db.create_all()
with db.session.begin():
    db.session.add_all([n1, n2])


# TODO напишите Class Based Views здесь

# Для проверки работоспособности запустите фаил
# и сделайте GET-запрос на адреса:
# - http://127.0.0.1/notes
# - http://127.0.0.1/notes/1
if __name__ == '__main__':
    app.run(debug=False)
