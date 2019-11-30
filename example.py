"""Get the data from an OpenSenseMap station."""
import asyncio

import aiohttp

from opensensemap_api import OpenSenseMap

SENSOR_ID = "5a528c40fa02ec000fe9058a"


async def main():
    """Sample code to retrieve the data from an OpenSenseMap station."""
    async with aiohttp.ClientSession() as session:
        station = OpenSenseMap(SENSOR_ID, loop, session)

        # Print details about the given station
        await station.get_data()

        print("Name:", station.name)
        print("Description:", station.description)
        print("Coordinates:", station.coordinates)

        print("PM 2.5:", station.pm2_5)
        print("PM 10:", station.pm10)

        print("Temperature:", station.temperature)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
