def squares(n):
    for i in range(n):
        yield i*i
for value in squares(5): print(value)