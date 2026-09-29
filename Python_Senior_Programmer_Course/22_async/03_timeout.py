import asyncio
async def slow(): await asyncio.sleep(2)
async def main():
    try: await asyncio.wait_for(slow(), timeout=0.2)
    except asyncio.TimeoutError: print("Timed out")
asyncio.run(main())