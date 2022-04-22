'''Decorator to time the execution time of a function.'''

from functools import wraps
from time import time
from decimal import Decimal


def timing(function):
    '''Simple timing function to measure execution time'''
    @wraps(function)
    def wrapper(*args, **kwargs):
        time_start = Decimal(time())
        result = function(*args, **kwargs)
        time_end = Decimal(time())
        total_time = f'Total Execution Time: {time_start - time_end} \n'
        function_name = f'** {function.__qualname__} ** \n'
        msg = function_name + total_time
        print(msg)
        return result
    return wrapper
