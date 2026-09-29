def report(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
report(1, 2, 3, status="PASS")