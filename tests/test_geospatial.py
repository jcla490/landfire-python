"""Geospatial utils tests."""
import geojson
import pytest
from fiona.errors import DriverError

from landfire.geospatial import (
    GeospatialDriver,
    get_bbox_from_file,
    get_bbox_from_polygon,
)


@pytest.fixture
def polygon_4326() -> geojson.Polygon:
    """Simply polygon (CRS: 4326) useful for spatial tests."""
    return geojson.Polygon(
        coordinates=[
            [
                [-107.70894964879554, 47.34869094341488],
                [-107.70894964879554, 46.5679909433598],
                [-106.0271812378708, 46.5679909433598],
                [-106.0271812378708, 47.34869094341488],
                [-107.70894964879554, 47.34869094341488],
            ]
        ],
        precision=8,
    )


@pytest.fixture
def polygon_3857() -> geojson.Polygon:
    """Simply polygon (CRS: 3857) useful for spatial tests. This is same as polygon_4326 location."""
    return geojson.Polygon(
        coordinates=[
            [
                [-11990105.42891634, 5999176.195931551],
                [-11990105.42891634, 5871842.088227722],
                [-11802891.825882928, 5871842.088227722],
                [-11802891.825882928, 5999176.195931551],
                [-11990105.42891634, 5999176.195931551],
            ]
        ],
        precision=8,
    )


def validate_bbox(bbox: str) -> bool:
    """Validate a rounded bbox to avoid issues with rounding on different workflow tests."""
    expected_bbox = [
        "-107.71",
        "46.57",
        "-106.03",
        "47.35",
    ]
    returned_bbox = [str(round(float(v), 2)) for v in bbox.split(" ")]
    return True if returned_bbox == expected_bbox else False


def test_get_bbox_from_polygon_same_crs(polygon_4326: geojson.Polygon) -> None:
    """Test get_bbox_from_polygon() returns a valid bounding box as string."""
    bbox: str = get_bbox_from_polygon(aoi_polygon=polygon_4326, crs="4326")
    assert isinstance(bbox, str)
    assert validate_bbox(bbox)


def test_get_bbox_from_polygon_diff_crs(polygon_3857: geojson.Polygon) -> None:
    """Test get_bbox_from_polygon() returns a valid bounding box as string in crs 4326 from 3857."""
    bbox: str = get_bbox_from_polygon(aoi_polygon=polygon_3857, crs="3857")
    assert isinstance(bbox, str)
    assert validate_bbox(bbox)


def test_get_bbox_from_file_shapefile() -> None:
    """Test get_bbox_from_file() returns a valid bounding box as string in crs 4326 from shapefile."""
    bbox: str = get_bbox_from_file(
        aoi_file_path="tests/data/test_shapefile/POLYGON.shp",
        driver=GeospatialDriver.shapefile,
    )
    assert isinstance(bbox, str)
    assert validate_bbox(bbox)


def test_get_bbox_from_file_shapefile_sad() -> None:
    """Test get_bbox_from_file() raises DriverError."""
    with pytest.raises(DriverError) as exc:
        get_bbox_from_file(
            aoi_file_path="tests/data/test_shapefile/POLYGON.shp",
            driver=GeospatialDriver.geojson,
        )
    assert (
        str(exc.value)
        == "Unable to read file with driver `GeoJSON`. Are you sure this is the correct driver for this file?"
    )


def test_get_bbox_from_file_geojson() -> None:
    """Test get_bbox_from_file() returns a valid bounding box as string in crs 4326 from geojson."""
    bbox: str = get_bbox_from_file(
        aoi_file_path="tests/data/test_4326.geojson",
        driver=GeospatialDriver.geojson,
    )
    assert isinstance(bbox, str)
    assert validate_bbox(bbox)


def test_get_bbox_from_file_geojson_no_driver() -> None:
    """Test get_bbox_from_file() returns a valid bounding box as string in crs 4326 from geojson with no provided driver."""
    bbox: str = get_bbox_from_file(
        aoi_file_path="tests/data/test_4326.geojson",
    )
    assert isinstance(bbox, str)
    assert validate_bbox(bbox)


def test_get_bbox_from_file_geojson_bad_driver() -> None:
    """Test get_bbox_from_file() returns a valid bounding box as string in crs 4326 from geojson with no provided driver."""
    driver = "BAD_DRIVER"
    with pytest.raises(RuntimeError) as exc:
        get_bbox_from_file(
            aoi_file_path="tests/data/test_4326.geojson",
            driver=driver,  # type: ignore
        )
    assert (
        str(exc.value)
        == f"`{driver}` is not a valid driver type! Supported drivers are {'.'.join([e.name for e in GeospatialDriver])}."
    )


def test_get_bbox_from_file_geojson_bad_path() -> None:
    """Test get_bbox_from_file() raises DriverError due to bad path."""
    with pytest.raises(RuntimeError) as exc:
        get_bbox_from_file(
            aoi_file_path="e",
        )
    assert (
        str(exc.value)
        == "Unable to read file. Are you sure the correct file path was provided?"
    )
