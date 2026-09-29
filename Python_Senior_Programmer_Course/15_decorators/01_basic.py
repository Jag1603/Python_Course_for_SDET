def log_call(func):
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper
@log_call
def add(a,b): return a+b
print(add(2,3))