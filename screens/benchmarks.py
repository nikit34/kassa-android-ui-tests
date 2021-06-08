import time


def timing(f):
    def timeit(*args, **kwargs):
        ts = time.time()
        result = f(*args, **kwargs)
        te = time.time()
        print(f'\ttiming: {f.__name__}{args[1:]} --> {te - ts} sec')
        return result
    return timeit