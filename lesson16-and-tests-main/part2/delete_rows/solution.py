from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import prettytable
from sqlalchemy import text
from guides_sql import CREATE_TABLE, INSERT_VALUES

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
with db.session.begin():
    db.session.execute(text(CREATE_TABLE))
    db.session.execute(text(INSERT_VALUES))


class Guide(db.Model):
    __tablename__ = 'guide'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String)
    full_name = db.Column(db.String)
    tours_count = db.Column(db.Integer)
    bio = db.Column(db.String)
    is_pro = db.Column(db.Boolean)
    company = db.Column(db.Integer)


def delete_guides():
    Guide.query.filter(Guide.id.in_([1, 4, 7])).delete(False)


delete_guides()
session = db.session()
cursor = session.execute("SELECT * FROM guide").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30

if __name__ == '__main__':
    print('БАЗА ДАННЫХ:')
    print(mytable)
