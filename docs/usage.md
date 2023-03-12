# Usage

## Quickstart

The simplest possible example requires simply initializing a `Landfire()` object for your area of interest and then submitting a request for data with `request_data()`, specifying the layers of interest and file location to download to (note the file does not need to exist yet, but the path does!).

This example downloads the minimum required layers to construct a landscape (.lcp) file for FlamMap.

```python
import landfire

# Obtain required layers for FlamMap landscape file
lf = landfire.Landfire(bbox="-107.70894965 46.56799094 -106.02718124 47.34869094")
lf.request_data(layers=["ELEV2020",   # elevation
                        "SLPD2020",   # slope degrees
                        "ASP2020",    # aspect
                        "220F40_22",  # fuel models
                        "220CC_22",   # canopy cover
                        "220CH_22",   # canopy height
                        "220CBH_22",  # canopy base height
                        "220CBD_22"], # canopy bulk density
                output_path="./test_flammap.zip")
```

Data will be downloaded to the `./test_flammap.zip` path!
