from contextlib import contextmanager
@contextmanager
def managed_resource():
    print("Acquire")
    try: yield "resource"
    finally: print("Release")
with managed_resource() as r: print(r)