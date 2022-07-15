# Имеется наполненная БД с таблицей guide и полуготовый код на фласке.
# Напишите представления для следующих ендпоинтов:
#
# Method: GET
# URL: /guides
# Response: [{guide_json}, {guide_json}, {guide_json}]
#
# Method: GET
# URL: /guides/1
# Response: { <guide_json> }
#
#
import json
import requests
from flask import Flask, jsonify
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from guides_sql import CREATE_TABLE, INSERT_VALUES

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False
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


@app.route("/guides")
def get_guides():
    # TODO допишите представления
    guides = Guide.query.all()

    response = []
    for guide in guides:
        response.append({
            "id": guide.id,
            "surname": guide.surname,
            "full_name": guide.full_name,
            "tours_count": guide.tours_count,
            "bio": guide.bio,
            "is_pro": guide.is_pro,
            "company": guide.company
        })

    return jsonify(response)


@app.route("/guides/<int:gid>")
def get_guide(gid):
    # TODO допишите представления
    guide = Guide.query.get(gid)
    guides = {
            "id": guide.id,
            "surname": guide.surname,
            "full_name": guide.full_name,
            "tours_count": guide.tours_count,
            "bio": guide.bio,
            "is_pro": guide.is_pro,
            "company": guide.company
        }

    return jsonify(guides)

# чтобы увидеть результат работы функций
# запустите фаил и
# перейдите по адресу:
# 127.0.0.1:5000/guides
# 127.0.0.1:5000/guides/1


if __name__ == "__main__":
    app.run(debug=True)
