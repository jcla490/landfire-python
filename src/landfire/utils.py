"""Landfire utilities."""
from typing import List
from typing import Tuple

import geojson


def polygon_to_bbox(aoi_polygon: geojson.Polygon) -> str:
    """Given a GeoJSON polygon, convert to a string bounding box with form (min_x, min_y, max_x, max_y).

    Args:
        aoi_polygon: polygon object representing your area of interest.

    Returns:
        bounding box of the polygon as a string.
    """
    coords: List[Tuple[float, ...]] = list(geojson.utils.coords(aoi_polygon))

    box: List[Tuple[float, ...]] = []
    for i in (0, 1):
        res = sorted(coords, key=lambda x: x[i])
        box.append((res[0][i], res[-1][i]))

    return f"{box[0][0]} {box[1][0]} {box[0][1]} {box[1][1]}"
