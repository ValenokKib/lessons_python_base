
def val_checker(manual_func):
    def _val_checker(func):
        def wrapper(num):
            if func(num):
                print(func(num))
            else:
                raise ValueError('некорректное значение {}'.format(num))
        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

a = calc_cube(-4)
