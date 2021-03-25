from . import ma


class PowerUserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "password", "user_type_id")

powerusers_schema = PowerUserSchema(many=True)
