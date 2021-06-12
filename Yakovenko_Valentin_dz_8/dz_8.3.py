from functools import wraps

def type_longer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        number = [i for i in (*args, *kwargs.values())]
        name = [f'{func.__name__}({i}: {type(i)})' for i in number]
        print(*name, *func(*args, **kwargs))
    return wrapper

@type_longer
def calc_cube(*x, **y):
    number = [i for i in (*x, *y.values()) if isinstance(i, int) or isinstance(i, float)]
    return [j ** 3 for j in number]

val = calc_cube(1, 2, 4, 3.3)


