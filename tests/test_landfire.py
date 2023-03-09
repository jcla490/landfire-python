"""Test suite for the landfire package."""
import tempfile
from typing import Any, Dict, Iterator
from unittest import mock
from unittest.mock import patch

import pytest

from landfire import Landfire


class MockResponse:
    """Mock response for request_data() tests."""

    def __init__(self, json_data: Dict[str, Any], status_code: int) -> None:
        """Class init."""
        self.json_data = json_data
        self.status_code = status_code

    def json(self) -> Dict[str, Any]:
        """Mock json func from Response."""
        return self.json_data

    def raise_for_status(self) -> None:
        """Mock raise_for_status func from Response."""
        return None

    def iter_content(self, chunk_size: int) -> Iterator[bytes]:
        """Mock iter_content func from Response."""
        return iter(
            [
                bytes(
                    "dummy text to write that is very cool",
                    encoding="utf-8",
                )
            ]
        )


def mocked_requests_get_all_success(*args: Any, **kwargs: Any) -> Any:
    """Build mock requests for all successful."""
    if "/submitJob" in kwargs["url"]:
        return MockResponse(
            {
                "jobId": "j2c9bd85a11324adb8b763747f2eafebb",
                "jobStatus": "esriJobSubmitted",
            },
            200,
        )
    elif "/jobs/" in kwargs["url"] and "Output_File" not in kwargs["url"]:
        return MockResponse(
            {
                "jobId": "j2c9bd85a11324adb8b763747f2eafebb",
                "jobStatus": "esriJobSucceeded",
                "results": {"Output_File": {"paramUrl": "results/Output_File"}},
                "inputs": {
                    "Layer_List": {"paramUrl": "inputs/Layer_List"},
                    "Area_of_Interest": {"paramUrl": "inputs/Area_of_Interest"},
                    "Output_Projection": {"paramUrl": "inputs/Output_Projection"},
                    "Resample_Resolution": {"paramUrl": "inputs/Resample_Resolution"},
                    "Edit_Rule": {"paramUrl": "inputs/Edit_Rule"},
                    "Edit_Mask": {"paramUrl": "inputs/Edit_Mask"},
                },
                "messages": [
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Job Finished",
                    }
                ],
            },
            200,
        )
    elif "Output_File" in kwargs["url"]:
        return MockResponse(
            {
                "paramName": "Output_File",
                "dataType": "GPDataFile",
                "value": {
                    "url": "https://lfps.usgs.gov/arcgis/rest/directories/arcgisjobs/landfireproductservice_gpserver/j2c9bd85a11324adb8b763747f2eafebb/scratch/j2c9bd85a11324adb8b763747f2eafebb.zip"
                },
            },
            200,
        )
    # We use iter_content() for the zip so the 'json' doesn't matter
    elif ".zip" in kwargs["url"]:
        return MockResponse(
            {"Test": "test"},
            200,
        )


def mocked_requests_get_submit_fail(*args: Any, **kwargs: Any) -> Any:
    """Build mock requests for initial submission failure when no job id."""
    if "/submitJob" in kwargs["url"]:
        return MockResponse(
            {
                "jobStatus": "esriJobSubmitted",
            },
            200,
        )


def mocked_requests_get_job_status_fail(*args: Any, **kwargs: Any) -> Any:
    """Build mock requests for job status fail."""
    if "/submitJob" in kwargs["url"]:
        return MockResponse(
            {
                "jobId": "j2c9bd85a11324adb8b763747f2eafebb",
                "jobStatus": "esriJobSubmitted",
            },
            200,
        )
    elif "/jobs/" in kwargs["url"] and "Output_File" not in kwargs["url"]:
        return MockResponse(
            {
                "jobId": "j2c9bd85a11324adb8b763747f2eafebb",
            },
            200,
        )


def mocked_requests_get_processing_fail(*args: Any, **kwargs: Any) -> Any:
    """Build mock requests for failure during processing."""
    if "/submitJob" in kwargs["url"]:
        return MockResponse(
            {
                "jobId": "j2c9bd85a11324adb8b763747f2eafebb",
                "jobStatus": "esriJobSubmitted",
            },
            200,
        )
    elif "/jobs/" in kwargs["url"] and "Output_File" not in kwargs["url"]:
        return MockResponse(
            {
                "jobId": "j2c9bd85a11324adb8b763747f2eafebb",
                "jobStatus": "esriJobFailed",
                "messages": [
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Sad failure",
                    }
                ],
            },
            200,
        )


@pytest.fixture
def landfire() -> Landfire:
    """Landfire fixture for use in other tests."""
    return Landfire(
        bbox="-107.70894965 46.56799094 -106.02718124 47.34869094",
        output_crs="4326",
        resample_res=31,
    )


@pytest.fixture
def temp_dir() -> Any:
    """A simple temporary directory fixture."""
    return tempfile.TemporaryDirectory()


def test_landfire_init() -> None:
    """Tests that Landfire object inits and user params are not changed on init."""
    lf = Landfire(
        bbox="-107.70894965 46.56799094 -106.02718124 47.34869094",
        output_crs="4326",
        resample_res=30,
    )
    assert lf.bbox == "-107.70894965 46.56799094 -106.02718124 47.34869094"
    assert lf.output_crs == "4326"
    assert lf.resample_res == 30


def test_resample_range_check_fail() -> None:
    """Tests that Landfire resample_res params fails range check."""
    with pytest.raises(ValueError) as exc:
        Landfire(
            bbox="-107.70894965 46.56799094 -106.02718124 47.34869094",
            output_crs="4326",
            resample_res=-1,
        )
    assert str(exc.value) == "resample_res must be between 30 and 9999 meters."


def test_request_data_bad_layers(landfire: Landfire) -> None:
    """Test provided user layers are invalid."""
    with pytest.raises(RuntimeError) as exc:
        landfire.request_data(layers=["BADLAYER"], output_path="")
    assert (
        str(exc.value)
        == "Specified layers do not match available layers from the LANDFIRE API. Please check your layer list and try again!"
    )


@patch("landfire.requests.get", side_effect=mocked_requests_get_all_success)
def test_landfire_download(
    mock_get: mock.Mock,
    landfire: Landfire,
    temp_dir: tempfile.TemporaryDirectory,  # type: ignore
) -> None:
    """Test successful responses and write to file."""
    landfire.request_data(
        layers=["map_zones"], output_path=f"{temp_dir.name}/test_data.zip"
    )
    temp_dir.cleanup()


@patch("landfire.requests.get", side_effect=mocked_requests_get_submit_fail)
def test_landfire_download_submit_fail(
    mock_get: mock.Mock,
    landfire: Landfire,
    temp_dir: tempfile.TemporaryDirectory,  # type: ignore
) -> None:
    """Test failure when no job id exists."""
    with pytest.raises(RuntimeError) as exc:
        landfire.request_data(
            layers=["map_zones"],
            output_path=f"{temp_dir.name}/test_data.zip",
        )
    assert (
        str(exc.value)
        == "Unable to obtain job ID for request! Please verify your request parameters and try again! If this problem continues, please raise an issue at https://github.com/FireSci/landfire/issues."
    )
    temp_dir.cleanup()


@patch("landfire.requests.get", side_effect=mocked_requests_get_job_status_fail)
def test_landfire_download_job_status_fail(
    mock_get: mock.Mock,
    landfire: Landfire,
    temp_dir: tempfile.TemporaryDirectory,  # type: ignore
) -> None:
    """Test failure when no job status exists."""
    with pytest.raises(RuntimeError) as exc:
        landfire.request_data(
            layers=["map_zones"],
            output_path=f"{temp_dir.name}/test_data.zip",
        )
    assert (
        str(exc.value)
        == "Could not obtain job status for job ID. Please try again! If this problem continues, please raise an issue at https://github.com/FireSci/landfire/issues."
    )
    temp_dir.cleanup()


@patch("landfire.requests.get", side_effect=mocked_requests_get_processing_fail)
def test_landfire_download_job_processing_fail(
    mock_get: mock.Mock,
    landfire: Landfire,
    temp_dir: tempfile.TemporaryDirectory,  # type: ignore
) -> None:
    """Test failure when processing fails."""
    with pytest.raises(RuntimeError) as exc:
        landfire.request_data(
            layers=["map_zones"],
            output_path=f"{temp_dir.name}/test_data.zip",
        )
    assert (
        str(exc.value)
        == "Encountered an error during job processing! Status was esriJobFailed and message was Sad failure."
    )
    temp_dir.cleanup()
