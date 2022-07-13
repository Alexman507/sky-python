from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
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
    guides = Guide.query.all()
    result = []
    for guide in guides:
        result.append({
            "id": guide.id,
            "surname": guide.surname,
            "full_name": guide.full_name,
            "tours_count": guide.tours_count,
            "bio": guide.bio,
            "is_pro": guide.is_pro,
            "company": guide.company,
        })
    return jsonify(result)


@app.route("/guides/<int:gid>")
def get_user(gid):
    guide = Guide.query.get(gid)
    guides = {
        "id": guide.id,
        "surname": guide.surname,
        "full_name": guide.full_name,
        "tours_count": guide.tours_count,
        "bio": guide.bio,
        "is_pro": guide.is_pro,
        "company": guide.company,
    }
    return jsonify(guides)


if __name__ == "__main__":
    app.run()
