# Задана модель Role, напишите схему
# и десериализацию так, чтобы она разбирала
# JSON данные и добавляла их в базу данных


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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


db.create_all()


class RoleSchema:
    # TODO напишите схему здесь
    pass


def create(data):
    # TODO напишите функцию здесь
    pass


if __name__ == "__main__":
    create({"id": 1, "name": "user"})
