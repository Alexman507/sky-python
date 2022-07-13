# Допишите модели гид(Guide) экскурсия (Excursion)
# в соответствии с ulm (схема расположена в корне папки задания)
#
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import prettytable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)


class Guide(db.Model):
    __tablename__ = 'guide'
    # TODO добавьте поля модели здесь


class Excursion(db.Model):
    __tablename__ = 'excursion'
    # TODO добавьте поля модели здесь

# Не удаляйте код ниже, он нужен для корректного
# отображения созданной вами модели


db.create_all()
session = db.session()
cursor_guide = session.execute("SELECT * from guide").cursor
mytable = prettytable.from_db_cursor(cursor_guide)
cursor_excursion = session.execute("SELECT * from excursion").cursor
mytable2 = prettytable.from_db_cursor(cursor_excursion)


if __name__ == '__main__':
    print(mytable)
    print(mytable2)
