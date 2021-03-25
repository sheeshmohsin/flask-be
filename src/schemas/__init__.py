from flask_marshmallow import Marshmallow

ma = Marshmallow()

from .power_user import powerusers_schema, GetRequestSchema
