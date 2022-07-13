from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import prettytable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(200))
    subject = db.Column(db.Text(200))
    price = db.Column(db.Integer)
    weeks = db.Column(db.Float)


db.create_all()
session = db.session()
cursor = session.execute(f"SELECT * from {Course.__tablename__}").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30

if __name__ == '__main__':
    print(mytable)
