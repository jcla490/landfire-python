"""Landfire."""
import attrs
from attrs import field
from attrs import frozen
from attrs import validators


__version__ = "0.0.0"
__all__ = ["landfire"]


@frozen
class Landfire:
    """Accessor class for LANDFIRE.

    Args:
        bbox: Bounding box with form `min_x min_y max_x max_y`. For example, `-107.70894965 46.56799094 -106.02718124 47.34869094`. Use util func `polygon_to_bbox()` to convert a GeoJSON polygon object to a suitable bounding box if needed.
        output_crs: Output coordinate reference system in well-known integer ID (EPSG) format. Defaults to `4326` or WGS84.
        resample_res: Resolution in meters for resampling output data. Defaults to 30 meters. Acceptable values are 30 to 9999 meters.

    """

    bbox: str = field(validator=validators.instance_of(str))
    output_crs: str = field(default="4326", validator=validators.instance_of(str))
    resample_res: int = field(default=30, validator=validators.instance_of(int))

    @resample_res.validator
    def resample_range_check(self, attribute: attrs.AttrsInstance, value: int) -> None:
        """Ensure resampling resolution is within allowable range."""
        print(attribute)
        if not 30 <= value <= 9999:
            raise ValueError("resample_res must be between 30 and 9999 meters.")


Landfire("test", "4326", 1)
# CRS conversion helper?
# bounding box or file helper
# ready made layer lists for common workflows (i.e., flammap)
