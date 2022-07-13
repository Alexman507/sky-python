# Напишите модель певец (Singer) с именем таблицы "singer"
# Для данной модели заданы следующие ограничения:
#
#
# #Таблица singer, описание колонок:
# Идентификатор - первичный ключ (PK) - id
# Имя - должно быть уникальным - name
# Возраст - не больше 35 лет - age
# Группа - не может быть Null (None) - group
#
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import prettytable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Singer(db.Model):
    __tablename__ = 'singer'
    # TODO напишите поля для модели Singer


db.drop_all()
db.create_all()
session = db.session()
cursor = session.execute("SELECT * from singer").cursor
mytable = prettytable.from_db_cursor(cursor)
session.close()

if __name__ == '__main__':
    print(mytable)
