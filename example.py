"""Get the data from an OpenSenseMap station."""
import asyncio

import aiohttp

from opensensemap_api import OpenSenseMap

SENSOR_ID = "63b83dcc6795ba0007794c93"


async def main():
    """Sample code to retrieve the data from an OpenSenseMap station."""
    async with aiohttp.ClientSession() as session:
        station = OpenSenseMap(SENSOR_ID, session)

        # Print details about the given station
        await station.get_data()

        print("Name:", station.name)
        print("Description:", station.description)
        print("Coordinates:", station.coordinates)
        print("Model:", station.model)
        print("Exposure:", station.exposure)

        print("PM 1.0:", station.pm1_0)
        print("PM 2.5:", station.pm2_5)
        print("PM 10:", station.pm10)

        print("Temperature:", station.temperature)
        print("Humidity:", station.humidity)
        print("Pressure:", station.air_pressure)
        print("Wind Speed:", station.wind_speed)
        print("Wind Direction:", station.wind_direction)
        print("Precipitation:", station.precipitation)
        print("Illuminance:", station.illuminance)
        print("UV Index:", station.uv)


if __name__ == "__main__":
    asyncio.run(main())
