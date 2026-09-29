import cProfile

def work(): return sum(i*i for i in range(10000))
cProfile.run("work()")