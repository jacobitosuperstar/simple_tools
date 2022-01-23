"""Decorator that ckecks the types of the arguments in the functions"""

from functools import wraps
from inspect import signature

class Base:
    @classmethod
    def __init_subclass__(cls):
        # instantiate the contracts
        for name, val in cls.__annotations__.items():
            contract = val() # class of the contract -> Integer()
            contract.__set_name__(cls, name)
            setattr(cls, name, contract)

class Typed(Contract):
    type = None
    @classmethod
    def check(cls, value):
        assert isinstance(value, cls.type), f'Expected {cls.type}'

def type_check(function):
    """Function that checks, if the input arguments are equial to the typed
    types"""
    sig = signature(function)
    ann = function.__annotations__
    @wraps(function)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            if name in ann:
                ann[name].check(val)
        return func(*args, **kwargs)
    return wrapper
