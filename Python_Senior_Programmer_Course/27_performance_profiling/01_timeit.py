from timeit import timeit
print(timeit("sum(range(1000))", number=10000))