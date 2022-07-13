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
class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(200))
    subject = db.Column(db.Text(200))
    price = db.Column(db.Integer)
    weeks = db.Column(db.Float)


# Не удаляйте код ниже, он нужен для корректного отображения
# созданной вами модели при запуске файла

db.drop_all()
db.create_all()
course1 = Course(id=1, title='Введение в Python', subject='Python', price=11000, weeks=3.5)
course2 = Course(id=2, title='Пишем на Spring', subject='Java', price=15000, weeks=8.0)
course3 = Course(id=3, title='Игры на Python', subject='Python', price=13500, weeks=5.0)
course4 = Course(id=4, title='Игры на Java', subject='Java', price=9000, weeks=4.5)


db.session.add_all([course1, course2, course3, course4])
db.session.commit()

session = db.session()
cursor = session.execute(f"SELECT * from {Course.__tablename__}").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30


if __name__ == '__main__':
    print(mytable)
