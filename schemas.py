from marshmallow import Schema, fields


class RequestSchema(Schema):
    id = fields.Str(dump_only=True)
    amount = fields.Str(required=True)
    status = fields.Str(required=True)
    household_id = fields.Str(required=True)

class HouseholdSchema(Schema):
    id = fields.Str(dump_only=True)
    area = fields.Str(required=True)
    address = fields.Str(required=True)
