from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import prettytable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Singer(db.Model):
    __tablename__ = 'singer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer, db.CheckConstraint("age < 35"))
    group = db.Column(db.String, nullable=False)


# Не удаляйте код ниже, он нужен для корректного
# отображения созданной вами модели

db.drop_all()
db.create_all()
session = db.session()
cursor = session.execute("SELECT * from singer").cursor
mytable = prettytable.from_db_cursor(cursor)

if __name__ == '__main__':
    print(mytable)
