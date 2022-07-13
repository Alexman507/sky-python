# Добавление пользователей
#
# Дана модель User и таблица user.
#
# Добавьте в базу данных сведения о пользователях
# в соответствии с таблицей:
#
# +----+------------------------+-----------+------------------+-----------------+
# | id |         email          |  password |    full_name     |     city_ru     |
# +----+------------------------+-----------+------------------+-----------------+
# | 1  |     novlu@mail.com     | mkdXjIjYM | Людмила Новикова | Санкт-Петербург |
# | 2  | tripper678@yahhaa.com  | eGGPtRKS5 | Андрей Васечкин  |      Москва     |
# | 3  | georgiberidze@mail.com | NWRV0Z9ZC |  Георги Беридзе  |     Тбилиси     |
# | 4  | oksi.laslas89@mail.com | TenhtQOjv |  Оксана Ласкина  |      Казань     |
# | 5  | vanyahot888@inmail.com | 5YGRPtYlw |   Иван Горячий   |       Сочи      |
# +----+------------------------+-----------+------------------+-----------------+
#
#
import prettytable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text(200))
    password = db.Column(db.Text(200))
    full_name = db.Column(db.Text(200))
    city_ru = db.Column(db.Text(200))


db.create_all()

# TODO напишите здесь код с запросом на добавление
# строк в таблицу
#
# Не удаляйте код ниже, он нужен для корректного отображения
# созданной вами модели при запуске файла

session = db.session()
cursor = session.execute(f"SELECT * from {User.__tablename__}").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30


if __name__ == '__main__':
    print(mytable)
