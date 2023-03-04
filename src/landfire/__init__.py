"""Landfire."""
from attrs import AttrsInstance
from attrs import field
from attrs import frozen
from attrs import validators

from landfire.search import ProductSearch


__version__ = "0.0.0"
__all__ = ["landfire"]

# URLs for making requests to LANDFIRE ArcGIS Rest Service
BASE_URL = "https://lfps.usgs.gov/arcgis/rest/services/LandfireProductService/GPServer/LandfireProductService"
REQUEST_URL = BASE_URL + "/submitJob?"
JOB_URL = BASE_URL + "/jobs/"


@frozen
class Landfire:
    """Accessor class for LANDFIRE.

    Args:
        bbox: Bounding box with form `min_x min_y max_x max_y`. For example, `-107.70894965 46.56799094 -106.02718124 47.34869094`. Use geospatial util func `get_bbox_from_polygon()` to convert a GeoJSON Polygon object or get_bbox_from_file() to convert a file to a suitable bounding box if needed.
        output_crs: Output coordinate reference system in well-known integer ID (WKID) format (EPSG). Defaults to `4326` or WGS84. See https://epsg.io for a full list of EPSG WKIDs.
        resample_res: Resolution in meters for resampling output data. Defaults to 30 meters. Acceptable values are 30 to 9999 meters.
    """

    bbox: str = field(validator=validators.instance_of(str))
    output_crs: str = field(default="4326", validator=validators.instance_of(str))
    resample_res: int = field(default=30, validator=validators.instance_of(int))

    # instantiate products for searching
    search = ProductSearch()

    @resample_res.validator
    def resample_range_check(self, attribute: AttrsInstance, value: int) -> None:
        """Ensure resampling resolution is within allowable range."""
        if not 30 <= value <= 9999:
            raise ValueError("resample_res must be between 30 and 9999 meters.")

    # def request_data(
    #     self, layers: List[str], output_path: Path, report_status: bool = True
    # ):
    #     """Request particular layers from Landfire.

    #     Args:
    #         layers: list of product layers.
    #         output_path: path object (including file name) where data will be downloaded to. For example, `~/tmp/output.tif`.

    #     """

    #     # Should validate layer list here

    #     # Make query URL
    #     params = {
    #         "Layer_List": layers,
    #         "Area_Of_Interest": self.bbox,
    #         "Output_Projection": self.output_crs,
    #         "Resample_Resolution": self.resample_res,
    #         "f": "JSON",
    #     }


lf = Landfire("1")
lf.search.search_products

# ready made layer lists for common workflows (i.e., flammap), minimum set of layers
#  latest elev, asp, slope
# export single bands instead of multi-band helper option would be dank
# name them after layer name
