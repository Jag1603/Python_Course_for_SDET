from concurrent.futures import ThreadPoolExecutor

def work(n): return n*n
with ThreadPoolExecutor(max_workers=4) as pool:
    print(list(pool.map(work, range(10))))