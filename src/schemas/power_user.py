from . import ma


class PowerUserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "user_type")


class GetRequestSchema:
    user_type = 'isdigit'
    before = 'isdigit'
    after = 'isdigit'


powerusers_schema = PowerUserSchema(many=True)
