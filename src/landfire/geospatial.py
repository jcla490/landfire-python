"""Landfire geospatial utilities. These exist for user convenience."""
from enum import Enum
from pathlib import Path
from typing import Optional


try:
    import geojson
    import geopandas as gpd
except ImportError as exc:
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


def polygon_to_bbox(aoi_polygon: geojson.Polygon) -> str:
    """Given a GeoJSON polygon, convert to a string bounding box with form `min_x, min_y, max_x, max_y`.

    Args:
        aoi_polygon: GeoJSON Polygon object representing your area of interest.

    Returns:
        bounding box of the polygon as a string.
    """
    gdf = gpd.GeoDataFrame(index=[0], geometry=[aoi_polygon]).to_crs(4326)

    return " ".join(str(x) for x in gdf.total_bounds)


def get_bbox_from_file(aoi_file_path: str, driver: Optional[GeospatialDriver]) -> str:
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
        RuntimeError if provided path is not able to be parsed as a Path object.
    """
    # Validate user provided path
    try:
        fpath = Path(aoi_file_path)
    except ValueError:
        raise RuntimeError(f"{aoi_file_path} is not a valid path!")

    # Validate user provided driver
    if driver:
        try:
            assert driver in GeospatialDriver
        except AssertionError:
            raise RuntimeError(
                f"{driver} is not a valid driver type! Supported drivers are {'.'.join([e for e in GeospatialDriver])}"
            )

        # Read file into gdf, leverage user provided driver
        gdf: gpd.GeoDataFrame = gpd.read_file(fpath, driver=driver)

    else:
        # Try to infer driver
        gdf = gpd.read_file(fpath)

    # 4326 is needed for Landfire API
    gdf = gdf.to_crs(4326)

    return " ".join(str(x) for x in gdf.total_bounds)
