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


db.drop_all()
db.create_all()

# TODO напишите здесь код с запросом на добавление
# строк в таблицу
#
user1 = User(id=1, email='novlu@mail.com', password='mkdXjIjYM', full_name='Людмила Новикова', city_ru='Санкт-Петербург')
user2 = User(id=2, email='tripper678@yahhaa.com', password='eGGPtRKS5', full_name='Андрей Васечкин', city_ru='Москва')
user3 = User(id=3, email='georgiberidze@mail.com', password='NWRV0Z9ZC', full_name='Георги Беридзе', city_ru='Тбилиси')
user4 = User(id=4, email='oksi.laslas89@mail.com', password='TenhtQOjv', full_name='Оксана Ласкина', city_ru='Казань')
user5 = User(id=5, email='vanyahot888@inmail.com', password='5YGRPtYlw', full_name='Иван Горячий', city_ru='Сочи')

db.session.add_all([user1, user2, user3, user4, user5])
db.session.commit()

# Не удаляйте код ниже, он нужен для корректного отображения
# созданной вами модели при запуске файла

session = db.session()
cursor = session.execute(f"SELECT * from {User.__tablename__}").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30


if __name__ == '__main__':
    print(mytable)
