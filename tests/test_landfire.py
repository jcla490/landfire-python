"""Test suite for the landfire package."""
from typing import Any, Dict

import pytest

from landfire import Landfire


@pytest.fixture
def landfire() -> Landfire:
    """Landfire fixture for use in other tests."""
    return Landfire(
        bbox="-107.70894965 46.56799094 -106.02718124 47.34869094",
        output_crs="4326",
        resample_res=30,
    )


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args: Any, **kwargs: Any) -> Any:
    class MockResponse:
        def __init__(self, json_data: Dict[str, Any], status_code: int) -> None:
            self.json_data = json_data
            self.status_code = status_code

        def json(self) -> Dict[str, Any]:
            return self.json_data

    if "/submitJob" in args[0]:
        return MockResponse(
            {
                "jobId": "j2c9bd85a11324adb8b763747f2eafebb",
                "jobStatus": "esriJobSubmitted",
            },
            200,
        )
    elif "/jobs/" in args[0]:
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
                        "description": 'Executing (LandfireProductService): LcpClip map_zones "-107.70894965 46.56799094 -106.02718124 47.34869094" 4326 # # # #',
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Start Time: Tue Mar  7 09:37:09 2023",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": 'Executing (LcpClip): LcpClip map_zones "-107.70894965 46.56799094 -106.02718124 47.34869094" 4326 # # # #',
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Start Time: Tue Mar  7 09:37:09 2023",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Running script LcpClip...",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "AOI: -107.70894965 46.56799094 -106.02718124 47.34869094",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Entering ValidateCoordinates()",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Entering DetermineRegion()",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "region: US_",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Exiting DetermineRegion()",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "US_MAP_ZONES",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Entering getISinfo()",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Exiting getISinfo()",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Start creating geotif",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Finished creating geotif",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Start zipping of files",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "All files zipped successfully.",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Job Finished",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Completed script LcpClip...",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Succeeded at Tue Mar  7 09:37:18 2023 (Elapsed Time: 9.47 seconds)",
                    },
                    {
                        "type": "esriJobMessageTypeInformative",
                        "description": "Succeeded at Tue Mar  7 09:37:18 2023 (Elapsed Time: 9.48 seconds)",
                    },
                ],
            },
            200,
        )
    elif "/results/Output_File" in args[0]:
        return (
            MockResponse(
                {
                    "paramName": "Output_File",
                    "dataType": "GPDataFile",
                    "value": {
                        "url": "https://lfps.usgs.gov/arcgis/rest/directories/arcgisjobs/landfireproductservice_gpserver/j2c9bd85a11324adb8b763747f2eafebb/scratch/j2c9bd85a11324adb8b763747f2eafebb.zip"
                    },
                },
                200,
            ),
        )


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


def test_request_data_bad_path(landfire: Landfire) -> None:
    """Test provided user path is invalid."""
    bad_path = "BADPATH/test.zip"
    with pytest.raises(RuntimeError) as exc:
        landfire.request_data(layers=["map_zones"], output_path=bad_path)
    assert (
        str(exc.value)
        == f"{bad_path} does not exist! Verify the path exists and the file name ends in `.zip`."
    )


# This is an integration test, class needs jesus
def test_landfire_download(landfire: Landfire) -> None:
    landfire.request_data(
        layers=["map_zones"],
        output_path="/Users/joshclark/Desktop/repos/firesci/landfire/tests/data/test_data.zip",
    )
