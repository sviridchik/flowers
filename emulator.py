import asyncio
from asyncio import exceptions

import aiohttp

from plants_base.choices import TypeChoice
from plants_base.models import Succulents

DEFAULT_TIMEOUT = 5


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response


async def f1():
    while True:
        # TODO raise ImproperlyConfigured(
        response = get(f"http://127.0.0.1:8000/plants_base/plants/{TypeChoice.MICROGREEN.value}/")
        print("hello from #1 coroutine", response)

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
    loop = asyncio.get_event_loop()
    try:
        asyncio.run(asyncio.wait_for(main(), DEFAULT_TIMEOUT))
    except exceptions.TimeoutError:
        print("the end")
