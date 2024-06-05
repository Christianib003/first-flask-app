from marshmallow import Schema, fields


class PlainRequestSchema(Schema):
    id = fields.Str(dump_only=True)
    amount = fields.Int(required=True)
    status = fields.Str(missing="pending")


class PlainHouseholdSchema(Schema):
    id = fields.Str(dump_only=True)
    area = fields.Str(required=True)
    address = fields.Str(required=True)


class RequestSchema(PlainRequestSchema):
    household_id = fields.Int(required=True, load_only=True)
    household = fields.Nested(PlainHouseholdSchema, dump_only=True)


class HouseholdSchema(PlainHouseholdSchema):
    requests = fields.Nested(PlainRequestSchema, many=True, dump_only=True)