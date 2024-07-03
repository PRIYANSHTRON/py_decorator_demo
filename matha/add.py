import os

def logger(func):
    def wrapper(a,b):
        log_dir = os.path.dirname(__file__)
        log_file = os.path.join(log_dir, 'log.txt')
        with open(log_file,'a') as f:
            f.write('addition function used\n')
        result = func(a,b)
        return result
    return wrapper

@logger
def add(a,b):
    return a+b