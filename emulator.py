import asyncio
import json
import logging
import random
from asyncio import exceptions

import aiohttp

# TODO for more serios fields
import faker

from COSTANTS import DISTRIBUTION_MAP
from plants_base.choices import TypeChoice

logging.basicConfig(level=logging.INFO)

with open("config.json") as f:
    data_constants_raw = json.load(f)
data_constants = {}
for i in range(len(data_constants_raw["VALUE_TO_CHANGE"])):
    node = data_constants_raw["VALUE_TO_CHANGE"][i]
    data_constants[node["field"]] = DISTRIBUTION_MAP[node["distribution"]](node["range"][0], node["range"][1])
    if "function" in node:
        data_constants[node["field"]] = DISTRIBUTION_MAP[node["function"]](data_constants[node["field"]])


async def choose_the_victim_plant(session):
    async with session.get(
        f"{data_constants_raw['BACKEND_URL']}/plants_base/plants/{TypeChoice.SUCCULENT.value}/"
    ) as response:
        response = await response.json()
    if len(response) > 0:
        victim_index = random.randint(0, len(response) - 1)
        victim = response[victim_index]
        logging.info(f"The tribut is has been chosen: plant with id = {victim['id']}")
        field_to_change_index = random.randint(0, len(data_constants_raw["FIELDS_TO_CHANGE"]) - 1)
        field_to_change = data_constants_raw["FIELDS_TO_CHANGE"][field_to_change_index]
        value = data_constants[field_to_change]
        async with session.patch(
            f"{data_constants_raw['BACKEND_URL']}/plants_base/plants/{TypeChoice.SUCCULENT.value}/{victim['id']}/",
            data={field_to_change: value},
        ) as response:
            response_patch = await response.json()

        status = response.status
        if status == 200:
            state = "successfully"
        else:
            state = "unsuccessfully"
        logging.info(f"Metric that was {state} changed is {field_to_change}, with value {value}")
        logging.info(response_patch)
    else:
        logging.warning(f"Metric wasn't changed , reason: {response.json}")
    await asyncio.sleep(1)


async def main():
    N = 3
    async with aiohttp.ClientSession() as session:
        while N > 0:
            N -= 1
            task1 = asyncio.create_task(choose_the_victim_plant(session))
            await asyncio.gather(task1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        asyncio.run(asyncio.wait_for(main(), data_constants_raw["DEFAULT_TIMEOUT"]))
    except exceptions.TimeoutError:
        print("the end")
