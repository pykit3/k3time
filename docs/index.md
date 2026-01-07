# k3time

[![Action-CI](https://github.com/pykit3/k3time/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3time/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3time/badge/?version=stable)](https://k3time.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3time)](https://pypi.org/project/k3time)

Time conversion utilities for parsing and formatting timestamps.

k3time is a component of [pykit3](https://github.com/pykit3) project: a python3 toolkit set.

## Installation

```bash
pip install k3time
```

## Quick Start

```python
import k3time

# Parse ISO format datetime
dt = k3time.parse('2017-01-24T07:51:59.000Z', 'iso')
print(dt)  # datetime.datetime(2017, 1, 24, 7, 51, 59)

# Format timestamp to ISO string
iso_str = k3time.format_ts(1485216000, 'iso')
print(iso_str)  # '2017-01-24T00:00:00.000Z'

# Format with custom pattern
formatted = k3time.format_ts(1485216000, '%Y-%m-%d')
print(formatted)  # '2017-01-24'

# Get current timestamp in various units
print(k3time.ts())  # seconds
print(k3time.ms())  # milliseconds
print(k3time.us())  # microseconds
```

## API Reference

::: k3time

## License

The MIT License (MIT) - Copyright (c) 2015 Zhang Yanpo (张炎泼)
