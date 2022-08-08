from marshmallow import Schema, fields


class Movie(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


class Director(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class Genre(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()