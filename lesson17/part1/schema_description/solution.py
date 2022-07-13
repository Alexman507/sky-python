from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    author = db.Column(db.String)
    year = db.Column(db.Integer)


db.create_all()

book = Book(id=1, name="buratino", author="narod", year=1999)

with db.session.begin():
    db.session.add(book)


class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    author = fields.Str()
    year = fields.Int()


def serialize():
    book_schema = BookSchema()
    result = Book.query.get(1)
    return book_schema.dump(result)


if __name__ == "__main__":
    print(json.dumps(serialize(), indent=4))
