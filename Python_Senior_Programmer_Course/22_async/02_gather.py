import asyncio
async def task(n):
    await asyncio.sleep(0.1)
    return n*n
async def main():
    results = await asyncio.gather(*(task(n) for n in range(5)))
    print(results)
asyncio.run(main())