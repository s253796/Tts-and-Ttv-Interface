import time
from functools import wraps

# Decorator 1: measure runtime
def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.3f} seconds")
        return result
    return wrapper

# Decorator 2: simple cache
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in cache:
            print("Using cached result")
            return cache[args]
        result = func(*args, **kwargs)
        cache[args] = result
        return result
    return wrapper
