import time

def retry(operation, attempts=3, delay=0.2):
    last=None
    for _ in range(attempts):
        try: return operation()
        except Exception as exc:
            last=exc; time.sleep(delay)
    raise last
