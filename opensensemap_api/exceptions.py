"""Exceptions for OpenSenseMap API client."""


class OpenSenseMapError(Exception):
    """General OpenSenseMap exception occurred."""

    pass


class OpenSenseMapConnectionError(OpenSenseMapError):
    """When a connection error is encountered."""

    pass


class OpenSenseMapNoDataAvailable(OpenSenseMapError):
    """When no data is available."""

    pass
