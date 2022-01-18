# this file was created for more convinient testing of emulator
import asyncio
from asyncio import exceptions

import aiohttp

from plants_base.choices import TypeChoice
from plants_base.data_for_tests import DATA_SUCCULENTS

DEFAULT_TIMEOUT = 5


async def post(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            json_response = await response.json()
            return json_response


async def f1():
    response = await post(
        f"http://127.0.0.1:8000/plants_base/plants/{TypeChoice.SUCCULENT.value}/", data=DATA_SUCCULENTS
    )
    response = await post(
        f"http://127.0.0.1:8000/plants_base/plants/{TypeChoice.SUCCULENT.value}/", data=DATA_SUCCULENTS
    )
    response = await post(
        f"http://127.0.0.1:8000/plants_base/plants/{TypeChoice.SUCCULENT.value}/", data=DATA_SUCCULENTS
    )

    print("hello from #1 coroutine", response)

    await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(f1())
    await asyncio.gather(task1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        asyncio.run(asyncio.wait_for(main(), DEFAULT_TIMEOUT))
    except exceptions.TimeoutError:
        print("the end")
