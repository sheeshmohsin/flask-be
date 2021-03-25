from schemas import GetRequestSchema

class PowerUserValidator(GetRequestSchema):

    def validate_int(self, arg_name, value):
        if value:
            validate_func = getattr(GetRequestSchema, arg_name)
            if getattr(value, validate_func)():
                return value
        return None
    
    def get_args(self, request):
        args = [x for x in dir(GetRequestSchema) if not x.startswith('__')]
        return { k: self.validate_int(k, request.args.get(k, None)) for k in args }
