"""Landfire."""
import logging
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import requests
from attrs import AttrsInstance, define, field, validators
from requests import Response

from landfire.product.search import ProductSearch


__version__ = "0.0.0"
__all__ = ["landfire"]

# URLs for making requests to LANDFIRE ArcGIS Rest Service
BASE_URL = "https://lfps.usgs.gov/arcgis/rest/services/LandfireProductService/GPServer/LandfireProductService"
REQUEST_URL = BASE_URL + "/submitJob?"
JOB_URL = BASE_URL + "/jobs/"

logger = logging.getLogger(__name__)


@define(frozen=True)
class Landfire:
    """Accessor for LANDFIRE data.

    Args:
        bbox: Bounding box with form `min_x min_y max_x max_y`. For example, `-107.70894965 46.56799094 -106.02718124 47.34869094`. Use geospatial util func `get_bbox_from_polygon()` to convert a GeoJSON Polygon object or get_bbox_from_file() to convert a file to a suitable bounding box if needed.
        output_crs: Output coordinate reference system in well-known integer ID (WKID) format (EPSG). Defaults to `4326` or WGS84. See https://epsg.io for a full list of EPSG WKIDs.
        resample_res: Resolution in meters for resampling output data. Defaults to 30 meters. Acceptable values are 30 to 9999 meters.
    """

    bbox: str = field(validator=validators.instance_of(str))
    output_crs: str = field(default="4326", validator=validators.instance_of(str))
    resample_res: int = field(default=30, validator=validators.instance_of(int))

    # instantiate products for searching
    search: ProductSearch = ProductSearch()
    # for validation
    all_layers: List[str] = search.get_layers()
    # base param payload
    base_params: Dict[str, Union[None, str, int]] = {
        "Layer_List": None,
        "Area_Of_Interest": bbox,
        "Output_Projection": output_crs,
        "Resample_Resolution": resample_res,
        "f": "JSON",
    }
    # request session
    session = requests.Session()

    @resample_res.validator
    def resample_range_check(self, attribute: AttrsInstance, value: int) -> None:
        """Ensure resampling resolution is within allowable range."""
        if not 30 <= value <= 9999:
            raise ValueError("resample_res must be between 30 and 9999 meters.")

    def __log_status(self, msg: str, show_status: bool) -> None:
        if show_status:
            logger.info(msg)

    def __validate_layers(self, layers: List[str]) -> None:
        """Validate user provided layers are available for download.

        Args:
            layers: List of user provided layers to validate

        Raises:
            RuntimeError if user provided layers do not match possible layers available for download.
        """
        try:
            assert all(layer in self.all_layers for layer in layers)
        except AssertionError:
            raise RuntimeError(
                "Specified layers do not match available layers from the LANDFIRE API. Please check your layer list and try again!"
            )

    def __submit_request(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        stream: Optional[bool] = None,
    ) -> Response:
        submit_req = self.session.get(url=url, params=params, stream=stream)
        submit_req.raise_for_status()
        return submit_req

    def request_data(
        self,
        layers: List[str],
        output_path: str,
        show_status: bool = True,
    ) -> None:
        """Request particular layers from Landfire.

        Args:
            layers: List of product layers.
            output_path: Path-like string where data will be downloaded to. Include file name and .zip extension. For example, `~/tmp/my_landfire_data/output.zip`.
            show_status: Boolean whether to log data request status.

        """
        # User layer validation
        self.__validate_layers(layers)

        # User path validation
        try:
            assert Path(output_path).exists()
        except AssertionError:
            raise RuntimeError(f"{output_path} does not exist!")

        # Add layer list to base_params
        self.base_params["Layer_List"] = ";".join(layers)

        # Submit initial request for layers
        submit_job_req = self.__submit_request(REQUEST_URL, self.base_params).json()

        # Get job id, check status of processing with exponential backoff
        if "jobId" in submit_job_req:
            job_id = submit_job_req["jobId"]
            status = submit_job_req["jobStatus"]
            self.__log_status("Job submitted! Processing request.", show_status)

            job_url = JOB_URL + job_id
            n = 0
            while status == "esriJobSubmitted" or status == "esriJobExecuting":
                n += 1
                backoff_sec = 2**n
                if n != 1:
                    self.__log_status(
                        f"Checking status of job in {backoff_sec} seconds...",
                        show_status,
                    )
                    time.sleep(backoff_sec)

                status_job_req = self.__submit_request(job_url, {"f": "json"}).json()

                if "jobStatus" in status_job_req:
                    status = status_job_req["jobStatus"]

                    # Obtain zip file URL
                    if status == "esriJobSucceeded":
                        data_path = status_job_req["results"]["Output_File"]["paramUrl"]
                        results_url = job_url + "/" + data_path
                        data_job_req = self.__submit_request(
                            results_url, params={"f": "json"}
                        ).json()
                        zip_url = data_job_req["value"]["url"]
                        self.__log_status(
                            f"Downloading data as .zip to {output_path}",
                            show_status,
                        )

                        # Last request to get the zip file
                        zip_job_req = self.__submit_request(zip_url, stream=True)
                        # Write to provided output path
                        with open(output_path, "wb") as fd:
                            for chunk in zip_job_req.iter_content(
                                chunk_size=1024 * 1024
                            ):
                                fd.write(chunk)
                        self.__log_status(
                            f"Data written successfully to {output_path}",
                            show_status,
                        )
                    # Still executing, display most recent processing step
                    elif status == "esriJobExecuting":
                        self.__log_status(
                            f"Still processing! Most recent message is `{status_job_req['messages'][-1]['description']}`",
                            show_status,
                        )

                    # Fail if processing error
                    else:
                        raise RuntimeError(
                            f"Encountered an error during job processing! {status_job_req['messages'][-1]['description']}"
                        )
                # Fail if no job status
                else:
                    raise RuntimeError(
                        "Could not obtain job status for job ID. Please try again! If this problem continues, please raise an issue at https://github.com/FireSci/landfire/issues."
                    )
        # Fail if no job id
        else:
            raise RuntimeError(
                "Unable to obtain job ID for request! Please verify your request parameters and try again! If this problem continues, please raise an issue at https://github.com/FireSci/landfire/issues."
            )
