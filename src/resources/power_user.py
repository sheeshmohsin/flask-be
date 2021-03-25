from flask import request
from flask_restful import Resource
from repositories import PowerUserRepository
from schemas import powerusers_schema
from validators import PowerUserValidator


class PowerUserResource(Resource, PowerUserValidator):
    """ Verbs related to users """

    def get(self):
        kwargs = self.get_args(request)
        poweruser_list = PowerUserRepository.filter(**kwargs)
        return powerusers_schema.dump(poweruser_list)
