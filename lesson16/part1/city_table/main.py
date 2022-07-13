# Городская таблица
# Определите поля для модели City по таблице city:
# +----+---------+------------+------------+
# | id |   name  | country_ru | population |
# +----+---------+------------+------------+
# | 1  |   Рим   |   Италия   |  2873000   |
# | 2  |  Милан  |   Италия   |  1333000   |
# | 3  | Венеция |   Италия   |   265000   |
# +----+---------+------------+------------+
#
#
import prettytable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class City(db.Model):
    __tablename__ = 'city'
    # TODO определите поля модели здесь
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    country_ru = db.Column(db.String)
    population = db.Column(db.Integer)




# Не удаляйте код ниже, он нужен для корректного отображения
# созданной вами модели при запуске файла
db.drop_all()
db.create_all()

rome = City(id=1, name='Рим', country_ru='Италия', population=2873000)
milan = City(id=2, name='Милан', country_ru='Италия', population=1333000)
venecia = City(id=3, name='Венеция', country_ru='Италия', population=265000)

db.session.add_all([rome, milan, venecia])
db.session.commit()
session = db.session()
cursor = session.execute("SELECT * from city").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30

if __name__ == '__main__':
    print(mytable)
