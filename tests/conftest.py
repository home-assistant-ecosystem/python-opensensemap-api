"""Shared test data for opensensemap_api tests."""
SENSOR_ID = "63b83dcc6795ba0007794c93"

MOCK_STATION_DATA = {
    "name": "Test Station",
    "description": "A test air quality station",
    "currentLocation": {
        "coordinates": [8.6821, 50.1109, 120.0],
        "type": "Point",
    },
    "exposure": "outdoor",
    "model": "homeV2Lora",
    "sensors": [
        {
            "title": "Temperature",
            "lastMeasurement": {"value": "21.50"},
        },
        {
            "title": "Temperatur",
            "lastMeasurement": {"value": "21.50"},
        },
        {
            "title": "Humidity",
            "lastMeasurement": {"value": "55.20"},
        },
        {
            "title": "rel. Luftfeuchte",
            "lastMeasurement": {"value": "55.20"},
        },
        {
            "title": "Air Pressure",
            "lastMeasurement": {"value": "1013.25"},
        },
        {
            "title": "Pressure",
            "lastMeasurement": {"value": "1013.25"},
        },
        {
            "title": "PM10",
            "lastMeasurement": {"value": "12.3"},
        },
        {
            "title": "PM2.5",
            "lastMeasurement": {"value": "6.7"},
        },
        {
            "title": "PM1.0",
            "lastMeasurement": {"value": "3.1"},
        },
        {
            "title": "Illuminance",
            "lastMeasurement": {"value": "500"},
        },
        {
            "title": "Beleuchtungsstärke",
            "lastMeasurement": {"value": "500"},
        },
        {
            "title": "UV Index",
            "lastMeasurement": {"value": "2"},
        },
        {
            "title": "UV",
            "lastMeasurement": {"value": "2"},
        },
        {
            "title": "Radioactivity",
            "lastMeasurement": {"value": "0.12"},
        },
        {
            "title": "Wind Speed",
            "lastMeasurement": {"value": "3.5"},
        },
        {
            "title": "Windgeschwindigkeit",
            "lastMeasurement": {"value": "3.5"},
        },
        {
            "title": "Wind Direction",
            "lastMeasurement": {"value": "270"},
        },
        {
            "title": "Windrichtung",
            "lastMeasurement": {"value": "270"},
        },
        {
            "title": "Precipitation",
            "lastMeasurement": {"value": "0.5"},
        },
        {
            "title": "Rain",
            "lastMeasurement": {"value": "0.5"},
        },
        {
            "title": "VCC",
            "lastMeasurement": {"value": "3.3"},
        },
    ],
}

MOCK_STATION_DATA_MINIMAL = {
    "name": "Minimal Station",
    "currentLocation": {
        "coordinates": [0.0, 0.0],
        "type": "Point",
    },
    "sensors": [],
}
