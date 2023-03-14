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

`landfire-python` is a wrapper around the [LANDFIRE][landfire] Products Service API, allowing users to obtain any of the available LANDFIRE data layers with just a few lines of code. This library was initially built to faciliate automated data ingest for wildfire modeling and analysis internally at [FireSci][firesci]. However, we're happy to open-source and maintain this tool to enable broader user of LANDFIRE data across the wildfire community! 🔥

[landfire]: https://landfire.gov/index.php
[firesci]: https://firesci.io/

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
- [attrs][attrs], [pydantic][pydantic], and [requests][requests] will be installed when you install the lib
- Optional dependencies included in the `geospatial` extra are [fiona][fiona], [geojson][geojson] and [geopandas][geopandas]

[attrs]: https://www.attrs.org/en/stable/index.html
[pydantic]: https://docs.pydantic.dev/
[requests]: https://requests.readthedocs.io/en/latest/
[fiona]: https://github.com/Toblerity/Fiona
[geojson]: https://python-geojson.readthedocs.io/en/latest/#
[geopandas]: https://geopandas.org/en/stable/

## Installation

```bash
pip install landfire
```

To use the geospatial tools found in `geospatial.py`, you'll need to install the extra dependencies:

```bash
pip install "landfire[geospatial]"
```

## Usage

The simplest possible example requires simply initializing a `Landfire()` object for your area of interest and then submitting a request for data with `request_data()`, specifying the layers of interest and file location to download to (note the file does not need to exist yet, but the path does!).

This example downloads the minimum required layers to construct a landscape (.lcp) file for FlamMap.

```python
import landfire

# Obtain required layers for FlamMap landscape file
lf = landfire.Landfire(bbox="-107.70894965 46.56799094 -106.02718124 47.34869094")
lf.request_data(layers=["ELEV2020",   # elevation
                        "SLPD2020",   # slope degrees
                        "ASP2020",    # aspect
                        "220F40_22",  # fuel models
                        "220CC_22",   # canopy cover
                        "220CH_22",   # canopy height
                        "220CBH_22",  # canopy base height
                        "220CBD_22"], # canopy bulk density
                output_path="./test_flammap.zip")
```

Please see the [documentation][documentation] for further information on possible options, geospatial utilities, and searching for products!

[documentation]: https://landfire-python.readthedocs.io/en/latest/usage.html

## Contributing

Contributions are very welcome! 🙏 To learn more, see the [contributor guide][contributor guide].

[contributor guide]: https://landfire-python.readthedocs.io/en/latest/contributing.html

## License

Distributed under the terms of the [MIT license][license], landfire-python is free and open source software.

[license]: https://landfire-python.readthedocs.io/en/latest/license.html

## Issues

If you encounter any problems, please [file an issue][file an issue] along with a detailed description! 🙌

[file an issue]: https://github.com/FireSci/landfire-python/issues

<!-- github-only -->
