# Задана модель Role, напишите схему
# и десериализацию так, чтобы она разбирала
# JSON данные и добавляла их в базу данных


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
import prettytable
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class RoleSchema(Schema):
    id = fields.Int()
    name = fields.Str()


db.create_all()


def create(data):
    role_schema = RoleSchema()
    role_dict = role_schema.load(data)
    role = Role(**role_dict)
    with db.session.begin():
        db.session.add(role)


if __name__ == "__main__":
    create({"id": 1, "name": "TestUser"})
    session = db.session()
    cursor = session.execute(f"SELECT * from {Role.__tablename__}").cursor
    mytable = prettytable.from_db_cursor(cursor)
    mytable.max_width = 30
    print(mytable)
