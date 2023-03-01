"""Utils tests."""
import geojson
import pytest

from landfire.geospatial import polygon_to_bbox


@pytest.fixture
def polygon() -> geojson.Polygon:
    """Simply polygon useful for spatial tests."""
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


def test_polygon_to_bbox(polygon: geojson.Polygon) -> None:
    """Test polygon_to_bbox() returns a valid bounding box as string."""
    bbox: str = polygon_to_bbox(aoi_polygon=polygon)
    assert isinstance(bbox, str)
    assert bbox == "-107.70894965 46.56799094 -106.02718124 47.34869094"
