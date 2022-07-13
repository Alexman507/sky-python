# Таблица сообщений
# Создайте модель Course по таблице course:
# +----+-------------------+---------+-------+-------+
# | id |       title       | subject | price | weeks |
# +----+-------------------+---------+-------+-------+
# | 1  | Введение в Python |  Python | 11000 |  3.5  |
# | 2  |  Пишем на Spring  |   Java  | 15000 |  8.0  |
# | 3  |   Игры на Python  |  Python | 13500 |  5.0  |
# | 4  |    Игры на Java   |   Java  |  9000 |  4.5  |
# +----+-------------------+---------+-------+-------+
#
#
import prettytable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# TODO определите модель здесь


# Не удаляйте код ниже, он нужен для корректного отображения
# созданной вами модели при запуске файла
db.create_all()
session = db.session()
cursor = session.execute(f"SELECT * from {Course.__tablename__}").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30


if __name__ == '__main__':
    print(mytable)
