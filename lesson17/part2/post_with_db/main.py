# У вас настроенный фласк,
# модель, пара записей в бд
# и схема для сериализации.
#
# - Вам необходимо создать Сlass based view, который позволяет
#   с помощью POST-запроса по адресу `/notes/` добавить
#   в базу данных запись о соответствующем объекте

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from prettytable import prettytable

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


# TODO напишите Class Based View здесь


# # # # # # # # # # # #                                    # Не удаляйте этот код, он нужен для
if __name__ == '__main__':                                 # имитации post-запроса и вывода
    client = app.test_client()                             # результата в терминал
    response = client.post('/notes/', json='')             # TODO для самопроверки вы можете добавить
    session = db.session()                                 # свой json в соответствующий аргумент
    cursor = session.execute("SELECT * FROM note").cursor  # функции post
    mytable = prettytable.from_db_cursor(cursor)
    mytable.max_width = 30
    print("БАЗА ДАННЫХ")
    print(mytable)
