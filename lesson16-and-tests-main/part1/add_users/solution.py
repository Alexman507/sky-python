from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import prettytable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text(200))
    password = db.Column(db.Text(200))
    full_name = db.Column(db.Text(200))
    city_ru = db.Column(db.Text(200))


db.create_all()
Ludmila = User(
    id=1,
    email="novlu@mail.com",
    password="mkdXjIjYM",
    full_name="Людмила Новикова",
    city_ru="Санкт-Петербург")
Andrew = User(
    id=2,
    email="tripper678@yahhaa.com",
    password="eGGPtRKS5",
    full_name="Андрей Васечкин",
    city_ru="Москва")
George = User(
    id=3,
    email="georgiberidze@mail.com",
    password="NWRV0Z9ZC",
    full_name="Георги Беридзе",
    city_ru="Тбилиси")
Oksana = User(
    id=4,
    email="oksi.laslas89@mail.com",
    password="TenhtQOjv",
    full_name="Оксана Ласкина",
    city_ru="Казань")
Ivan = User(
    id=5,
    password="5YGRPtYlw",
    full_name="Иван Горячий",
    email='vanyahot888@inmail.com',
    city_ru="Сочи")

users = (Ludmila, Andrew, George, Oksana, Ivan)

with db.session.begin():
    db.session.add_all(users)

session = db.session()
cursor = session.execute(f"SELECT * from {User.__tablename__}").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30

if __name__ == '__main__':
    print(mytable)
