# coding=utf-8
from threading import Semaphore, Timer
from functools import wraps


def rate_limit(calls_count, interval):
    """
    Rate limit decorator
    :param calls_count: count of calls in an interval
    :param interval: limit time in seconds
    """
    def decorator(func):
        semaphore = Semaphore(calls_count)

        @wraps(func)
        def wrapper(*args, **kwargs):
            semaphore.acquire()

            try:
                return func(*args, **kwargs)
            finally:
                timer = Timer(interval, semaphore.release)
                timer.setDaemon(True)
                timer.start()

        return wrapper
    return decorator
