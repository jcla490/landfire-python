# landfire-python

[![PyPI](https://img.shields.io/pypi/v/landfire.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/landfire.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/landfire)][python version]
[![License](https://img.shields.io/pypi/l/landfire)][license]

[![Read the documentation at https://landfire-python.readthedocs.io/](https://img.shields.io/readthedocs/landfire-python/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/FireSci/landfire-python/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/FireSci/landfire-python/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/landfire/
[status]: https://pypi.org/project/landfire/
[python version]: https://pypi.org/project/landfire
[read the docs]: https://landfire-python.readthedocs.io/
[tests]: https://github.com/FireSci/landfire-python/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/FireSci/landfire-python
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Features

`landfire-python` is a wrapper around the [LANDFIRE] Products Service API, allowing users to obtain any of the available LANDFIRE data layers with just a few lines of code. This library was initially built to faciliate automated data ingest for wildfire modeling and analysis internally at [FireSci]. However, we're happy to open-source and maintain this tool to enable broader user of LANDFIRE data across the wildfire community!

### Supported LANDFIRE functionality

- Clipping requested data to a specific bounding box
- Reprojection of output data coordinate system to user-specified well-known integer ID format
- Specifying a list of data product layers and obtaining a multi-band .tif output
- Modifying the resampling resolution

### Additional functionality

- Search functionality to allow users to search for products by LANDFIRE version, name, product theme, product code, or availability regions (US, AK, HI)
- Geospatial helpers to obtain suitable bounding box from a GeoJSON polygon or file (GeoJSON, ESRI Shapefile, ESRIJSON, CSV, FlatGeobuf, SQLite)
- Robust model and enumerations of LANDFIRE products
- User input validation to reduce potential failed API jobs and server load

### Planned but not currently supported

- Specifying edit rules for fuels data (requires a great deal of user-input validation)
- Specifying an edit mask for edit rules (requires more LANDFIRE API i/o implementation)
- Note the LANDFIRE API does not currently provide support for insular regions
- We will add new products here as they become available

## Requirements

- python >=3.8, <3.12
- [attrs], [pydantic], and [requests] will be installed when you install the lib
- Optional dependencies included in the `geospatial` extra are [geojson] and [geopandas]

## Installation

```bash
pip install landfire
```

To use the geospatial tools found in `geospatial.py`, you'll need to install the extra dependencies:

```bash
pip install "landfire[geospatial]"
```

## Usage

Please see the [documentation] for details.

## Contributing

Contributions are very welcome! To learn more, see the [contributor guide].

## License

Distributed under the terms of the [MIT license][license], landfire-python is free and open source software.

## Issues

If you encounter any problems, please [file an issue] along with a detailed description!s

[file an issue]: https://github.com/FireSci/landfire-python/issues
[landfire]: https://landfire.gov/index.php
[firesci]: https://firesci.io/
[attrs]: https://www.attrs.org/en/stable/index.html
[pydantic]: https://docs.pydantic.dev/
[requests]: https://requests.readthedocs.io/en/latest/
[geojson]: https://python-geojson.readthedocs.io/en/latest/#
[geopandas]: https://geopandas.org/en/stable/
[documentation]: https://landfire-python.readthedocs.io/en/latest/usage.html

<!-- github-only -->

[license]: https://github.com/FireSci/landfire-python/blob/main/LICENSE
[contributor guide]: https://github.com/FireSci/landfire-python/blob/main/CONTRIBUTING.md
