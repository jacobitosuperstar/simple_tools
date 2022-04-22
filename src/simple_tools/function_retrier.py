"""Decorator for debugging messages using the `print` statement or logging the
infomation in a .log file"""

from functools import wraps
from .debugger import print_debug


def retry(*, max_tries: int = 0):
    """Simple function retrier that retries a function upon failing a certain
    ammount of times. The initial values of repetition is `0`."""
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            tries = 0
            while True:
                try:
                    return function(*args, **kwargs)
                except Exception as error:
                    tries += 1
                    if tries >= max_tries:
                        raise error
                else:
                    break
        return wrapper
    return decorator
