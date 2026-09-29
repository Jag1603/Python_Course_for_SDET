from functools import wraps
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("LOG", func.__name__)
        return func(*args, **kwargs)
    return wrapper
@log
def hello(): return "hello"
print(hello.__name__)