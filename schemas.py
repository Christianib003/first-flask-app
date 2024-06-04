from marshmallow import Schema, fields


class RequestSchema(Schema):
    request_id = fields.Str(dump_only=True)
    amount = fields.Str(required=True)
    status = fields.Str(required=True)
    household_id = fields.Str(required=True)

class HouseholdSchema(Schema):
    household_id = fields.Str(dump_only=True)
    area = fields.Str(required=True)
    address = fields.Str(required=True)
