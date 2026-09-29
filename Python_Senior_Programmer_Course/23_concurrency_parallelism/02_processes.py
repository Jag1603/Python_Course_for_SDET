from concurrent.futures import ProcessPoolExecutor

def square(n): return n*n
if __name__ == "__main__":
    with ProcessPoolExecutor() as pool:
        print(list(pool.map(square, range(10))))