"""
Time convertion utils.

    >>> parse('2017-01-24T07:51:59.000Z', 'iso')
    datetime.datetime(2017, 1, 24, 7, 51, 59)
    >>> format_ts(1485216000, 'iso')
    '2017-01-24T00:00:00.000Z'
    >>> format_ts(1485216000, '%Y-%m-%d')
    '2017-01-24'

"""

from .tm import (
    datetime_to_ts,
    format,
    format_ts,
    formats,
    is_timestamp,
    ms,
    ns,
    parse,
    parse_to_ts,
    to_sec,
    ts,
    ts_to_datetime,
    us,
    utc_datetime_to_ts,
)

__all__ = [
    "datetime_to_ts",
    "format",
    "format_ts",
    "formats",
    "is_timestamp",
    "ms",
    "ns",
    "parse",
    "parse_to_ts",
    "to_sec",
    "ts",
    "ts_to_datetime",
    "us",
    "utc_datetime_to_ts",
]


def __getattr__(name: str) -> str:
    # importlib.metadata takes about 20 ms to import, so it is loaded only
    # when __version__ is read
    if name != "__version__":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from importlib.metadata import version

    return version("k3time")
