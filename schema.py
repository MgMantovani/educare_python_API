from marshmallow import Schema, fields, validate

class AlunoSchema(Schema):
    nome = fields.Str(required=True, validate=validate.Length(min=2, max=80))
    email = fields.Email(required=True)
    idade = fields.Int(required=True)
