def receiver():
    value = yield "ready"
    yield value * 2
r = receiver(); print(next(r)); print(r.send(10))