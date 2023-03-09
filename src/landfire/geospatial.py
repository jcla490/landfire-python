"""Landfire geospatial utilities. These exist for user convenience."""
from enum import Enum
from pathlib import Path
from typing import Optional

from fiona.errors import DriverError


try:
    import geojson
    import geopandas as gpd
except ImportError as exc:  # pragma: no cover
    raise RuntimeError(
        f"Failed to import `{exc.name}`."
        f"Please install `landfire[geospatial]` in order to use functions in geospatial.py."
    )


class GeospatialDriver(str, Enum):
    """Supported geospatial drivers for get_bbox_from_file()."""

    geojson = "GeoJSON"
    shapefile = "ESRI Shapefile"
    csv = "CSV"
    esrijson = "ESRIJSON"
    sqlite = "SQLite"
    flatgeobuf = "FlatGeobuf"


def get_bbox_from_polygon(aoi_polygon: geojson.Polygon, crs: str = "4326") -> str:
    """Given a GeoJSON polygon, convert to a string bounding box with form `min_x, min_y, max_x, max_y` in CRS 4326 (WGS84).

    Args:
        aoi_polygon: GeoJSON Polygon object representing your area of interest.
        crs: Coordinate reference system in well-known integer ID (WKID) format (EPSG). Defaults to `4326` or WGS84. See https://epsg.io for a full list of EPSG WKIDs.

    Returns:
        bounding box of the GeoJSON Polygon object as a string.
    """
    gdf = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[aoi_polygon]).to_crs(4326)

    return " ".join(str(x) for x in gdf.total_bounds)


def get_bbox_from_file(
    aoi_file_path: str, driver: Optional[GeospatialDriver] = None
) -> str:
    """Given a particular file, convert all features to one string bounding box with form `min_x, min_y, max_x, max_y`. CRS will be discovered from file automatically and converted to 4326 (WGS84) if needed.

    Supported file drivers are found in enum GeospatialDriver and are:
    - GeoJSON
    - ESRI Shapefile
    - ESRIJSON
    - CSV
    - FlatGeobuf
    - SQLite

    Args:
        aoi_file_path: Path-like string to area of interest file.
        driver: Optional file driver (see supported drivers above). Use GeospatialDriver to specify the driver (i.e. `GeospatialDriver.geojson`, `GeospatialDriver.shapefile`, etc.). If no file driver is provided, will attempt to infer file type from file extension. If no file extension or provided driver, will infer as a shapefile.

    Returns:
        bounding box of the as a string.

    Raises:
        RuntimeError: If provided path is not able to be parsed as a Path object or if provided driver is not a valid member of GeospatialDriver enum.
        DriverError: If driver and file type do not match.

    """
    # Validate user provided path
    try:
        fpath = Path(aoi_file_path)
    except ValueError:
        raise RuntimeError(f"`{aoi_file_path}` is not a valid path.")

    # Validate user provided driver
    if driver:
        try:
            assert driver in GeospatialDriver._value2member_map_
        except (AssertionError, TypeError):
            raise RuntimeError(
                f"`{driver}` is not a valid driver type! Supported drivers are {'.'.join([e.name for e in GeospatialDriver])}."
            )

        try:
            # Read file into gdf, leverage user provided driver
            gdf: gpd.GeoDataFrame = gpd.read_file(fpath, driver=driver)
        except DriverError:
            raise DriverError(
                f"Unable to read file with driver `{driver}`. Are you sure this is the correct driver for this file?"
            )
    else:
        # Try to infer driver
        try:
            gdf = gpd.read_file(fpath)
        except DriverError:
            raise RuntimeError(
                "Unable to read file. Are you sure the correct file path was provided?"
            )
    # 4326 is needed for Landfire API
    gdf = gdf.to_crs(4326)

    return " ".join(str(x) for x in gdf.total_bounds)
