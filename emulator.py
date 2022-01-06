import asyncio

@asyncio.coroutine
def f1():
    while (True):
        print("hello from #1 coroutine")
        yield from asyncio.sleep(1)



@asyncio.coroutine
def f2():
    while (True):
        print("hello from #2 coroutine")
        yield from asyncio.sleep(1)

@asyncio.coroutine
def main():
    task1 = asyncio.ensure_future(f1())
    task2 = asyncio.ensure_future(f2())

    yield from asyncio.gather(task1,task2)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    # main()
