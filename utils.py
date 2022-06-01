import time
from functools import wraps


def time_f(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} took {time.time() - t1} seconds")
        return result

    return measure_time