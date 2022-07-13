from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import prettytable
from sqlalchemy import text
from guides_sql import CREATE_TABLE, INSERT_VALUES

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
with db.session.begin():
    db.session.execute(text(CREATE_TABLE))
    db.session.execute(text(INSERT_VALUES))


class Guide(db.Model):
    __tablename__ = 'guide'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String)
    full_name = db.Column(db.String)
    tours_count = db.Column(db.Integer)
    bio = db.Column(db.String)
    is_pro = db.Column(db.Boolean)
    company = db.Column(db.Integer)


def do_request():
    result = db.session.query(Guide).filter(Guide.tours_count > 3).all()
    return result


# не удаляйте код ниже, он необходим
# для выдачи результата запроса


mytable = prettytable.PrettyTable()
mytable.field_names = [
    'id', 'surname', 'full_name',
    'tours_count', 'bio', 'is_pro', 'company']

rows = [[x.id, x.surname, x.full_name,
         x.tours_count, x.bio, x.is_pro, x.company] for x in do_request()]
mytable.add_rows(rows)
mytable.max_width = 30

if __name__ == "__main__":
    print('Запрос возвращает следующие записи:')
    print(mytable)
