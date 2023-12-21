"""An openSenseMap API Python client."""
import asyncio
import logging
import socket

import aiohttp
import async_timeout

from . import exceptions

_LOGGER = logging.getLogger(__name__)
_INSTANCE = "https://api.opensensemap.org/boxes/{id}"

_TITLES = {
    "Air Pressure": (
        "Pressure",
        "Luftdruck",
        "Ilmanpaine",
    ),
    "Humidity": (
        "rel. Luftfeuchte",
        "rel. Humidity",
        "Ilmankosteus",
        "Kosteus",
    ),
    "Illuminance": (
        "Beleuchtungsstärke",
        "Valoisuus",
        "Valaistuksen voimakkuus",
        "Ambient Light",
    ),
    "Temperature": (
        "Temperatur",
        "Lämpötila",
    ),
    "UV": (
        "UV Index",
        "UV-Intensität",
        "UV-säteily",
    ),
    "Precipitation": (
        "Rain",
        "Regen",
        "Niederschlag",
    ),
    "Wind Speed": ("Windgeschwindigkeit",),
    "Wind Direction": ("Windrichtung",),
}


class OpenSenseMap(object):
    """A class for handling connections with the openSenseMap API."""

    def __init__(self, sensor_id, session):
        """Initialize the connection the openSenseMap API."""
        self._session = session
        self.data = {}
        self.base_url = _INSTANCE.format(id=sensor_id)

    async def get_data(self):
        """Get details of OpenSenseMap station."""
        try:
            async with async_timeout.timeout(5):
                response = await self._session.get(self.base_url)

            _LOGGER.info("Response from OpenSenseMap API: %s", response.status)
            self.data = await response.json()
            _LOGGER.debug(self.data)

        except (asyncio.TimeoutError, aiohttp.ClientError, socket.gaierror):
            _LOGGER.error("Can not load data from openSenseMap API")
            raise exceptions.OpenSenseMapConnectionError

    @property
    def description(self):
        """Return the description of the station."""
        try:
            return self.data["description"]
        except KeyError:
            return None

    @property
    def name(self):
        """Return the name of the station."""
        return self.data["name"]

    @property
    def coordinates(self):
        """Return the coordinates of the station."""
        return self.data["currentLocation"]["coordinates"]

    @property
    def exposure(self):
        """Return the exposure of the station."""
        try:
            return self.data["exposure"]
        except KeyError:
            return None

    @property
    def model(self):
        """Return the model of the station."""
        try:
            return self.data["model"]
        except KeyError:
            return None

    @property
    def pm10(self):
        """Return the particulate matter 10 value."""
        return self.get_value("PM10")

    @property
    def pm2_5(self):
        """Return the particulate matter 2.5 value."""
        return self.get_value("PM2.5")

    @property
    def pm1_0(self):
        """Return the particulate matter 1.0 value."""
        return self.get_value("PM1.0")

    @property
    def temperature(self):
        """Return the temperature of a station."""
        return self.get_value("Temperature")

    @property
    def humidity(self):
        """Return the humidity of a station."""
        return self.get_value("Humidity")

    @property
    def vcc(self):
        """Return the current VCC of a station."""
        return self.get_value("VCC")

    @property
    def air_pressure(self):
        """Return the current air pressure of a station."""
        return self.get_value("Air Pressure")

    @property
    def illuminance(self):
        """Return the current illuminance of a station."""
        return self.get_value("Illuminance")

    @property
    def uv(self):
        """Return the current UV value of a station."""
        return self.get_value("UV")

    @property
    def radioactivity(self):
        """Return the current radioactivity value of a station."""
        return self.get_value("Radioactivity")

    @property
    def wind_speed(self):
        """Return the current wind speed value of a station."""
        return self.get_value("Wind Speed")

    @property
    def wind_direction(self):
        """Return the current wind direction value of a station."""
        return self.get_value("Wind Direction")

    @property
    def precipitation(self):
        """Return the current precipitation value of a station."""
        return self.get_value("Precipitation")

    def get_value(self, key):
        """Extract a value for a given key."""
        for title in _TITLES.get(key, ()) + (key,):
            try:
                value = [
                    entry["lastMeasurement"]["value"]
                    for entry in self.data["sensors"]
                    if entry["title"].casefold() == title.casefold()
                    and "lastMeasurement" in entry
                    and "value" in entry["lastMeasurement"]
                ][0]
                return value
            except (IndexError, TypeError):
                pass
        return None
