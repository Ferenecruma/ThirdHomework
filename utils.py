import time
from functools import wraps


def time_f(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        fn(*args, **kwargs)
        elapsed_time = time.time() - t1
        print(f"{fn.__name__} took {elapsed_time} seconds")
        return elapsed_time

    return measure_time