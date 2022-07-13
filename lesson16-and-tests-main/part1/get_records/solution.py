from flask import Flask
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
import prettytable
from users_sql import CREATE_TABLE, INSERT_VALUES

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
with db.session.begin():
    db.session.execute(text(CREATE_TABLE))
    db.session.execute(text(INSERT_VALUES))


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    full_name = db.Column(db.String)
    city = db.Column(db.Integer)
    city_ru = db.Column(db.String)


def get_all():
    all_users = User.query.all()
    return all_users


def get_one(id):
    one_user = User.query.get(id)
    return one_user


if __name__ == "__main__":
    mytable_one = prettytable.PrettyTable()
    mytable_all = prettytable.PrettyTable()
    columns = [
        'id', 'email', 'password',
        'full_name', 'city', 'city_ru']
    mytable_one.field_names = columns
    mytable_all.field_names = columns
    rows = [[x.id, x.email, x.password,
             x.full_name, x.city, x.city_ru] for x in get_all()]
    obj = get_one(1)
    row = [obj.id, obj.email, obj.password,
           obj.full_name, obj.city,
           obj.city_ru]

    mytable_all.add_rows(rows)
    mytable_one.add_row(row)
    print('get_one:')
    print(mytable_one)
    print('get_all:')
    print(mytable_all)
