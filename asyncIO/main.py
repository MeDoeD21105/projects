import asyncio
import time


async def cor1(start):
    print(f"ДО СНА КОР1 {time.time() - start:0.0f}")
    await asyncio.sleep(1)
    print(f"Posle sleep COR2 {time.time() - start:0.0f}")


async def cor2(start):
    print(f"ДО СНА КОР2 {time.time() - start:0.0f}")
    await asyncio.sleep(1)
    print(f"Posle sleep COR2 {time.time() - start:0.0f}")


async def main():
    start = time.time()
    await asyncio.gather(cor1(start), cor2(start))
    print(f"Pose FINISHED Main {time.time() - start:0.00f}")


asyncio.run(main())
