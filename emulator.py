import asyncio


async def f1():
    while True:
        print("hello from #1 coroutine")
        await asyncio.sleep(1)


async def f2():
    while True:
        print("hello from #2 coroutine")
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(f1())
    task2 = asyncio.create_task(f2())

    await asyncio.gather(task1, task2)


if __name__ == "__main__":
    asyncio.run(main())
