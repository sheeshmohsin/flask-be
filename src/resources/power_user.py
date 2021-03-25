from flask.json import jsonify
from flask_restful import Resource
from repositories import PowerUserRepository
from schemas import powerusers_schema


class PowerUserResource(Resource):
    """ Verbs related to users """

    def get(self):
        poweruser_list = PowerUserRepository.filter()
        print (poweruser_list)
        print (type(poweruser_list))
        return powerusers_schema.dump(poweruser_list)
