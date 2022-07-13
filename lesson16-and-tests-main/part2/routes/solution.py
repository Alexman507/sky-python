from flask import Flask, request, jsonify
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


def instance_to_dict(instance):
    """
    Serialize implementation
    """
    return {
        "id": instance.id,
        "surname": instance.surname,
        "full_name": instance.full_name,
        "tours_count": instance.tours_count,
        "bio": instance.bio,
        "is_pro": instance.is_pro,
        "company": instance.company,
    }


@app.route("/guides")
def get_all_and_by_tours_count():
    """
    The view contains requests to DB about:
    - all guides
    - guides filtered by tours_count field
    """
    tours_count = request.args.get("tours_count")
    result = []
    if not tours_count:
        guides = Guide.query.all()
        for guide in guides:
            result.append(instance_to_dict(guide))
        return jsonify(result)
    guides = Guide.query.filter_by(tours_count=tours_count)
    for guide in guides:
        result.append(instance_to_dict(guide))
    return jsonify(result)


@app.route("/guides/<int:gid>", methods=['GET'])
def get_one(gid):
    guide = Guide.query.get(gid)
    return jsonify(instance_to_dict(guide))


@app.route("/guides/<int:gid>/delete")
def delete_guide(gid):
    guide = Guide.query.get(gid)
    db.session.delete(guide)
    db.session.commit()
    return jsonify("")


@app.route("/guides", methods=['POST'])
def create_guide():
    data = request.json
    guide = Guide(
        surname=data.get('surname'),
        full_name=data.get('full_name'),
        tours_count=data.get('tours_count'),
        bio=data.get('bio'),
        is_pro=data.get('is_pro'),
        company=data.get('company')
    )
    db.session.add(guide)
    db.session.commit()
    return jsonify(instance_to_dict(guide))


if __name__ == "__main__":
    app.run()
