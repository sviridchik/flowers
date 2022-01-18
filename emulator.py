import asyncio
import logging
import random
from asyncio import exceptions

import aiohttp

# TODO for more serios fields
import faker

from plants_base.choices import TypeChoice

FIELDS_TO_CHANGE = ["level_of_complexity", "spraying"]
VALUE_TO_CHANGE = [random.uniform(0, 5), bool(random.randint(0, 1))]
DEFAULT_TIMEOUT = 5
logging.basicConfig(level=logging.INFO)


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            json_response = await response.json()
            return json_response


async def patch(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.patch(url, data=data) as response:
            json_response = await response.json()
            return json_response, response.status


async def choose_the_victim_plant():
    # the hungry games )
    response = await get(f"http://127.0.0.1:8000/plants_base/plants/{TypeChoice.SUCCULENT.value}/")
    victim_id = random.randint(0, len(response) - 1)
    victim = response[victim_id]
    logging.info(f"The tribut is has been chosen: plant with id = {victim['id']}")
    field_to_change = random.randint(0, len(FIELDS_TO_CHANGE) - 1)
    value = VALUE_TO_CHANGE[field_to_change]
    response_patch, status = await patch(
        f"http://127.0.0.1:8000/plants_base/plants/{TypeChoice.SUCCULENT.value}/{victim['id']}/",
        data={FIELDS_TO_CHANGE[field_to_change]: value},
    )
    if status == 200:
        state = "successfully"
    else:
        state = "unsuccefully"
    logging.info(f"Metric that was {state} changed is {FIELDS_TO_CHANGE[field_to_change]}, with value {value}")
    logging.info(response_patch)
    await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(choose_the_victim_plant())
    await asyncio.gather(task1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        asyncio.run(asyncio.wait_for(main(), DEFAULT_TIMEOUT))
    except exceptions.TimeoutError:
        print("the end")
