from flask import current_app as app
from flask_restx import Api, fields as flask_fields
from marshmallow import fields as marshmallow_fields

api: Api = app.config['api']

TYPE_MAPPING = {
    marshmallow_fields.Float: flask_fields.Float,
    marshmallow_fields.Int: flask_fields.Integer,
    marshmallow_fields.String: flask_fields.String,
    marshmallow_fields.Number: flask_fields.Integer,
    marshmallow_fields.DateTime: flask_fields.DateTime
}


def convert_and_register_model(schema_name, schema_data):
    schema_fields = getattr(schema_data, "_declared_fields")
    coverted_schema = {}

    for field in schema_fields:
        coverted_schema[field] = TYPE_MAPPING[type(schema_fields[field])]

    api.model(name=schema_name, model=coverted_schema)

    return coverted_schema
