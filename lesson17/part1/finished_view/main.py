# У вас есть модель с книгами и несколько
# записей в БД. Напишите представление которое
# обрабатывает эндпоинт /books/ и возвращает
# полный список книг, используя сериализацию.
# Данные по одной записи в базе должны выглядеть так:
#    {
#      "id": 1,
#      "name": "buratino",
#      "author": "narod",
#      "year": 1999
#    }

# Исходный код
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.Integer)


class BookSchema:
    # TODO определите здесь схему сериализации
    pass

# С помощью данного отрезка кода мы создаём
# таблицу во временной базе данных и добавляем
# 2 записи, которые в последующем будем получать


db.create_all()
b1 = Book(id=1, name="Гарри Поттер", author="Джоан Роулинг", year=1992)
b2 = Book(id=2, name="Граф Монте Кристо", author="Александр Дюма", year=1854)

with db.session.begin():
    db.session.add_all([b1, b2])

# ######

# TODO напишите роут здесь


# чтобы проверить результат работы
# отправьте GET-запрос на адрес 127.0.0.1/books/
if __name__ == '__main__':
    app.run(debug=True)
