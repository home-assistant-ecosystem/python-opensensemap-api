"""Tests for the opensensemap_api package."""
import asyncio
import socket
from unittest.mock import AsyncMock, MagicMock

import aiohttp
import pytest

from opensensemap_api import OpenSenseMap
from opensensemap_api.exceptions import OpenSenseMapConnectionError

from .conftest import (
    MOCK_STATION_DATA,
    MOCK_STATION_DATA_MINIMAL,
    SENSOR_ID,
)


def _make_station(data=None):
    """Create an OpenSenseMap instance pre-loaded with data."""
    session = MagicMock()
    station = OpenSenseMap(SENSOR_ID, session)
    if data is not None:
        station.data = data
    return station


class TestInitialization:
    """Tests for OpenSenseMap initialisation."""

    def test_base_url_contains_sensor_id(self):
        station = _make_station()
        assert SENSOR_ID in station.base_url

    def test_initial_data_is_empty(self):
        station = _make_station()
        assert station.data == {}


class TestProperties:
    """Tests for OpenSenseMap station metadata properties."""

    def test_name(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.name == "Test Station"

    def test_description(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.description == "A test air quality station"

    def test_description_missing_returns_none(self):
        station = _make_station(MOCK_STATION_DATA_MINIMAL)
        assert station.description is None

    def test_coordinates(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.coordinates == [8.6821, 50.1109, 120.0]

    def test_exposure(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.exposure == "outdoor"

    def test_exposure_missing_returns_none(self):
        station = _make_station(MOCK_STATION_DATA_MINIMAL)
        assert station.exposure is None

    def test_model(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.model == "homeV2Lora"

    def test_model_missing_returns_none(self):
        station = _make_station(MOCK_STATION_DATA_MINIMAL)
        assert station.model is None


class TestSensorValues:
    """Tests for OpenSenseMap sensor value properties."""

    def test_temperature(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.temperature == "21.50"

    def test_humidity(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.humidity == "55.20"

    def test_air_pressure(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.air_pressure == "1013.25"

    def test_pm10(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.pm10 == "12.3"

    def test_pm2_5(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.pm2_5 == "6.7"

    def test_pm1_0(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.pm1_0 == "3.1"

    def test_illuminance(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.illuminance == "500"

    def test_uv(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.uv == "2"

    def test_radioactivity(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.radioactivity == "0.12"

    def test_wind_speed(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.wind_speed == "3.5"

    def test_wind_direction(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.wind_direction == "270"

    def test_precipitation(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.precipitation == "0.5"

    def test_vcc(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.vcc == "3.3"

    def test_missing_sensor_returns_none(self):
        station = _make_station(MOCK_STATION_DATA_MINIMAL)
        assert station.temperature is None
        assert station.humidity is None
        assert station.pm10 is None


class TestGetValue:
    """Tests for the get_value() helper and _TITLES alias resolution."""

    def test_get_value_by_exact_title(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.get_value("PM10") == "12.3"

    def test_get_value_case_insensitive(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.get_value("pm10") == "12.3"
        assert station.get_value("PM10") == "12.3"

    def test_temperature_alias_temperatur(self):
        """'Temperatur' (German) should resolve via _TITLES to temperature."""
        data = {
            **MOCK_STATION_DATA_MINIMAL,
            "sensors": [
                {"title": "Temperatur", "lastMeasurement": {"value": "18.0"}}
            ],
        }
        station = _make_station(data)
        assert station.temperature == "18.0"

    def test_humidity_alias_rel_luftfeuchte(self):
        data = {
            **MOCK_STATION_DATA_MINIMAL,
            "sensors": [
                {
                    "title": "rel. Luftfeuchte",
                    "lastMeasurement": {"value": "60.0"},
                }
            ],
        }
        station = _make_station(data)
        assert station.humidity == "60.0"

    def test_air_pressure_alias_pressure(self):
        data = {
            **MOCK_STATION_DATA_MINIMAL,
            "sensors": [
                {"title": "Pressure", "lastMeasurement": {"value": "1015.0"}}
            ],
        }
        station = _make_station(data)
        assert station.air_pressure == "1015.0"

    def test_illuminance_alias_beleuchtungsstaerke(self):
        data = {
            **MOCK_STATION_DATA_MINIMAL,
            "sensors": [
                {
                    "title": "Beleuchtungsstärke",
                    "lastMeasurement": {"value": "200"},
                }
            ],
        }
        station = _make_station(data)
        assert station.illuminance == "200"

    def test_uv_alias_uv_index(self):
        data = {
            **MOCK_STATION_DATA_MINIMAL,
            "sensors": [
                {"title": "UV Index", "lastMeasurement": {"value": "3"}}
            ],
        }
        station = _make_station(data)
        assert station.uv == "3"

    def test_wind_speed_alias_windgeschwindigkeit(self):
        data = {
            **MOCK_STATION_DATA_MINIMAL,
            "sensors": [
                {
                    "title": "Windgeschwindigkeit",
                    "lastMeasurement": {"value": "5.0"},
                }
            ],
        }
        station = _make_station(data)
        assert station.wind_speed == "5.0"

    def test_wind_direction_alias_windrichtung(self):
        data = {
            **MOCK_STATION_DATA_MINIMAL,
            "sensors": [
                {"title": "Windrichtung", "lastMeasurement": {"value": "90"}}
            ],
        }
        station = _make_station(data)
        assert station.wind_direction == "90"

    def test_precipitation_alias_rain(self):
        data = {
            **MOCK_STATION_DATA_MINIMAL,
            "sensors": [
                {"title": "Rain", "lastMeasurement": {"value": "1.0"}}
            ],
        }
        station = _make_station(data)
        assert station.precipitation == "1.0"

    def test_sensor_without_last_measurement_returns_none(self):
        data = {
            **MOCK_STATION_DATA_MINIMAL,
            "sensors": [{"title": "Temperature"}],
        }
        station = _make_station(data)
        assert station.temperature is None

    def test_sensor_with_empty_last_measurement_returns_none(self):
        data = {
            **MOCK_STATION_DATA_MINIMAL,
            "sensors": [{"title": "Temperature", "lastMeasurement": {}}],
        }
        station = _make_station(data)
        assert station.temperature is None

    def test_unknown_key_returns_none(self):
        station = _make_station(MOCK_STATION_DATA)
        assert station.get_value("NonExistentSensor") is None


class TestGetData:
    """Tests for the async get_data() method."""

    async def test_get_data_populates_data(self):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.json = AsyncMock(return_value=MOCK_STATION_DATA)

        mock_session = MagicMock()
        mock_session.get = AsyncMock(return_value=mock_response)

        station = OpenSenseMap(SENSOR_ID, mock_session)
        await station.get_data()

        assert station.data == MOCK_STATION_DATA
        assert station.name == "Test Station"

    async def test_get_data_raises_on_timeout(self):
        mock_session = MagicMock()
        mock_session.get = AsyncMock(side_effect=asyncio.TimeoutError)

        station = OpenSenseMap(SENSOR_ID, mock_session)
        with pytest.raises(OpenSenseMapConnectionError):
            await station.get_data()

    async def test_get_data_raises_on_client_error(self):
        mock_session = MagicMock()
        mock_session.get = AsyncMock(
            side_effect=aiohttp.ClientError("connection refused")
        )

        station = OpenSenseMap(SENSOR_ID, mock_session)
        with pytest.raises(OpenSenseMapConnectionError):
            await station.get_data()

    async def test_get_data_raises_on_gaierror(self):
        mock_session = MagicMock()
        mock_session.get = AsyncMock(
            side_effect=socket.gaierror("name resolution failed")
        )

        station = OpenSenseMap(SENSOR_ID, mock_session)
        with pytest.raises(OpenSenseMapConnectionError):
            await station.get_data()
