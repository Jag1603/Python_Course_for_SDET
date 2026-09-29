def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(times)]
        return wrapper
    return decorator
@repeat(3)
def greet(): return "Hi"
print(greet())