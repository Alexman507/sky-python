# У вас имеется настроенный фласк, модель,
# пара записей в бд и схема для сериализации.
#
# - Вам необходимо создать Сlass based view который позволяет
#   с помощью GET-запроса по адресу `/books` получить
#   список всех сущностей, имеющихся в базе данных
#

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app. config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 2}

db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.Integer)


class BookSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    author = fields.Str()
    year = fields.Int()


book_schema = BookSchema()
books_schema = BookSchema(many=True)

api = Api(app)
book_ns = api.namespace('books')

b1 = Book(id=1, name="Гарри Поттер", author="Джоан Роулинг", year=1992)
b2 = Book(id=2, name="Граф Монте Кристо", author="Александр Дюма", year=1854)

db.drop_all()
db.create_all()

with db.session.begin():
    db.session.add_all([b1, b2])


# TODO напишите Class Based View здесь


# для проверки работоспособности запустите фаил
# и зайдите в браузере на адрес http://127.0.0.1/books

if __name__ == '__main__':
    app.run(debug=False)
