def printlog(func):
    def wrapper(*args, **kwargs):
        print('CALLING:', func.__name__)
        return func(*args, **kwargs)
    return wrapper


@printlog
def f(a, b):
    return a + b


print(f(3, 5))


@printlog
def square(n):
    return n * n


print(square(f(1, 1)))
