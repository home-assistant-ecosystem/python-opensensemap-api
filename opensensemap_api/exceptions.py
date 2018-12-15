"""Exceptions for openSenseMap API client."""


class OpenSenseMapError(Exception):
    """General openSenseMap exception occurred."""

    pass


class OpenSenseMapConnectionError(OpenSenseMapError):
    """When a connection error is encountered."""

    pass


class OpenSenseMapNoDataAvailable(OpenSenseMapError):
    """When no data is available."""

    pass
