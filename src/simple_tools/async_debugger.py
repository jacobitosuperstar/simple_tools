"""Decorator for debugging messages using the logging module of async functions
in a .log file"""

from functools import wraps
import logging
import os
import concurrent.futures


# keeping the workers = 1 ensures that we log in the order that the functions
# are called
executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)


def __logger_object(path: str, logger_name:str):
    """Creates and return the logger object. Requires a path because it tries
    to create the path that you put in the `logging_debug` function, if it
    isn't created, no worries, it uses it no problem."""
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    # checking and creating the file if it doesn't exist.
    if os.path.isfile(f"{path}"):
        pass
    else:
        head_tail = os.path.split(f"{path}")
        path_dir = head_tail[0]
        # path_file = head_tail[1]
        os.makedirs(f"{path_dir}", exist_ok=True)
        open(f"{path}", "w").close()
    # file where we are going to log
    logger_file = logging.FileHandler(f"{path}")
    # logger format
    logger_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(logger_format)
    logger_file.setFormatter(formatter)
    # add handler to logger object
    logger.addHandler(logger_file)
    print(type(logger))
    return logger


def async_logging_debug(
    *,
    prefix: str = None,
    path: str = "./logs/error.log",
    logger_name: str = "ErrorLog",
):
    """Simple Debugger which creates the required files in the given path (It
    creates folders and files no problem) or it can use an already existing one
    without any problem.

    it ONLY uses NAMED ARGUMENTS, positional arguments are a Big NoNo, as you
    want real structure from the function callings, and those are:

    prefix -> String : The prefix that you would use to grep or search in the
                       log file.
    path -> String: The Path that you will use to store the log files that you
                    are creating. If the path doesn't exist the funcion will
                    create it for you. If no path is given it would create an
                    error.log file with the path BASE_DIR/logs/error.log"""
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            logger = __logger_object(path, logger_name)
            try:
                return function(*args, **kwargs)
            except Exception:
                msg = (
                    f"{prefix} "
                    "Oh No, something happened in the function "
                    f"{function.__qualname__}"
                )
                logger.exception(msg)
                raise
        return wrapper
    return decorator
