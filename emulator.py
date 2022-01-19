import asyncio
import json
import logging
import random
from asyncio import exceptions

import aiohttp

# TODO for more serios fields
import faker

from plants_base.choices import TypeChoice

logging.basicConfig(level=logging.INFO)

with open("config.json") as f:
    data_constants = json.load(f)

for i in range(len(data_constants["VALUE_TO_CHANGE"])):
    data_constants["VALUE_TO_CHANGE"][i] = eval(data_constants["VALUE_TO_CHANGE"][i])


async def choose_the_victim_plant():
    async with aiohttp.ClientSession() as session:
        # the hungry games )
        async with session.get(
            f"{data_constants['BACKEND_URL']}/plants_base/plants/{TypeChoice.SUCCULENT.value}/"
        ) as response:
            response = await response.json()
        if len(response) > 0:
            victim_index = random.randint(0, len(response) - 1)
            victim = response[victim_index]
            logging.info(f"The tribut is has been chosen: plant with id = {victim['id']}")
            field_to_change = random.randint(0, len(data_constants["FIELDS_TO_CHANGE"]) - 1)
            value = data_constants["VALUE_TO_CHANGE"][field_to_change]

            async with session.patch(
                f"{data_constants['BACKEND_URL']}/plants_base/plants/{TypeChoice.SUCCULENT.value}/{victim['id']}/",
                data={data_constants["FIELDS_TO_CHANGE"][field_to_change]: value},
            ) as response:
                response_patch = await response.json()

            status = response.status
            if status == 200:
                state = "successfully"
            else:
                state = "unsuccessfully"
            logging.info(
                f"Metric that was {state} changed is {data_constants['FIELDS_TO_CHANGE'][field_to_change]}, with value {value}"
            )
            logging.info(response_patch)
        else:
            logging.info("there is nothing to change")

    await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(choose_the_victim_plant())
    await asyncio.gather(task1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        asyncio.run(asyncio.wait_for(main(), data_constants["DEFAULT_TIMEOUT"]))
    except exceptions.TimeoutError:
        print("the end")
