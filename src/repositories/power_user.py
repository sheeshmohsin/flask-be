""" Defines the user repository """

from models import PowerUser


class PowerUserRepository:
    """ The repository for the user model """

    @staticmethod
    def filter(user_type=None, before=None, after=None):
        pagination_kwargs = {'before': before, 'after': after}
        filter_kwargs = { 'user_type' : user_type }
        if user_type:
            data = PowerUser.query.filter_by(**filter_kwargs) \
                .infinite_paginate(**pagination_kwargs).limit(10)
        else:
            data = PowerUser.query.infinite_paginate(**pagination_kwargs) \
                .limit(10)
        return data
