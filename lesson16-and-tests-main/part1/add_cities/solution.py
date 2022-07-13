from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import prettytable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)


class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    country_ru = db.Column(db.String)
    population = db.Column(db.Integer)


db.create_all()

Rome = City(
    id=1,
    name="Рим",
    country_ru="Италия",
    population=28730000)

Milan = City(
    id=2,
    name="Милан",
    country_ru="Италия",
    population=1333000)

Venice = City(
    id=3,
    name="Венеция",
    country_ru="Италия",
    population=265000)

Istanbul = City(
    id=4,
    name="Стамбул",
    country_ru="Турция",
    population=108950000)

Kemer = City(
    id=5,
    name="Кемер",
    country_ru="Турция",
    population=22421)

cities = (Rome, Milan, Venice, Istanbul, Kemer)

with db.session.begin():
    db.session.add_all(cities)

session = db.session()
cursor = session.execute(f"SELECT * from {City.__tablename__}").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30

if __name__ == '__main__':
    print(mytable)
