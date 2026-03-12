# Usage

## Quickstart

The simplest possible example requires simply initializing a `Landfire` object for a bounding box of interest and then submitting a request for data with `request_data()`, specifying the layers of interest and file location to download to (note that the file does not need to exist yet, but the path to the file should be valid).

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

## Searching for Products

There are many datasets available from LANDFIRE across various versions, regions, and themes. `landfire-python` provides a mechanism for searching all of the available products from the LANDFIRE API using the `ProductSearch` class. This class has several parameters for searching:

- `names`: search for the explicit name of products you're looking for.
- `codes`: search for the explicit product codes.
- `themes`: find all products matching a particular theme(s) (e.g., fuel, fire_regime, disturbance, vegetation, etc.). Use the `ProductTheme` enum.
- `versions`: find all products matching a particular LANDFIRE year/version release (e.g., 2001, 2012, 2014, 2020). Use the `ProductVersion` enum.
- `region`: find all products covering a particular geographic region(s) (i.e., US, AK, HI). Use the `ProductRegion` enum.

An example of a search for fire regime products for Alaska from LANDFIRE 2020 (v2.2.0) is found below. We call `get_products()` on the `ProductSearch` to return a list of `Products`. If you just want the layers without any of the information about the `Product`, use `get_layers()`.

```python
from landfire.product.search import ProductSearch
from landfire.product.enums import ProductRegion, ProductTheme, ProductVersion

search: List[Product] = ProductSearch(
        regions=[ProductRegion.AK],
        versions=[ProductVersion.lf_2020],
        themes=[ProductTheme.vegetation]
)
search_products = search.get_products()
# ...returns 3 Products
```

The result of the example is a list of `Products`. Each `Product` is a [pydantic][pydantic] model and thus its fields can be accessed with dot notation:

```python
for product in search_products: print(product.name)
# existing vegetation cover 2022
# existing vegetation height 2022
# existing vegetation type 2020
```

Each `Product` also has a list of `Availability` models that provides information on the product availability (region and possible layers) for each particular LANDFIRE version:

```python
# Grab the first product (existing vegetation cover 2022), and first availability object (LANDFIRE 2020):
search_products[0].availability[0]
# ...returns
# ProductAvailability(version=<ProductVersion.lf_2020: '2.2.0'>,
#                     regions=[<ProductRegion.US: 'US'>,
#                              <ProductRegion.AK: 'AK'>,
#                              <ProductRegion.HI: 'HI'>],
#                     layers=['105SCLASS'])
```

From here you can grab the layers for use in your request by using `.layers` on the above. However, we recommend using `get_layers()` on the search object to get the layers much easier:

```python
search.get_layers()
# ...returns
# ['220EVC_22', '220EVH_22', '220EVT']
```

You can pass this list of layers to your `Landfire()` object to get data from the LANDFIRE API!

> If you're a more visual person, you can also check out the [LANDFIRE product availability table][landfire product availability table]! There are also several utilities in `landfire.product.utils` that might be helpful for working with products!

[landfire product availability table]: https://lfps.usgs.gov/helpdocs/productstable.html
[pydantic]: https://docs.pydantic.dev/usage/models/

## Using the Geospatial Utilities

We provide some functionality to make it easier to obtain the bounding box necessary for input to LANDFIRE.

### Obtaining a Bounding Box from a GeoJSON Polygon

If you're working with GeoJSON data, you can simply pass a GeoJSON polygon object to `get_bbox_from_polygon()`

```python
import geojson
from landfire.geospatial import get_bbox_from_polygon

my_cool_polygon = geojson.Polygon(
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

bbox = get_bbox_from_polygon(aoi_polygon=my_cool_polygon, crs = "3857")  # web-mercator crs
# ...returns
# -107.70894964999998 46.56799093999999 -106.02718124000002 47.34869093999999
```

Note, the LANDFIRE API requires the bounding box geometry to be WGS84 (EPSG:4326). If you are providing a polygon in a different coordinate system, specify the well-known ID using the `crs` parameter like above and the function will reproject it for you.

### Obtaining a Bounding Box from a File

Another helpful function is `get_bbox_from_file()`, allowing you to provide file containing many features and get back a 'total' bounding box that encompasses all of the features. For example, if you were performing analysis on multiple fires across a National Forest, it might be less burdensome to simply obtain LANDFIRE data for all the fires at once instead of creating multiple landscapes for each.

We currently support the following file formats: - GeoJSON - ESRI Shapefile - ESRIJSON - CSV - FlatGeobuf - SQLite

There is no need to provide a CRS, it will be discovered from the file automatically and converted to 4326 (WGS84) if needed. However, it is helpful to provide the driver type via the `driver` parameter using the GeospatialDriver enumeration (although this function will try to detect the file type automatically if one is not provided).

```python
from landfire.geospatial import get_bbox_from_file, GeospatialDriver

bbox = get_bbox_from_file(
        aoi_file_path="test_fire_polygon.geojson",
        driver=GeospatialDriver.geojson,
)
# ...returns
# -107.70894964999998 46.56799093999999 -106.02718124000002 47.34869093999999
```

## Requesting Data

### Using the Landfire class

As shown in the quickstart, obtaining data is quite easy once you have a bounding box and list of layers in hand. Provide a location to save the file to and watch it go!

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

# Data will be downloaded to the `./test_flammap.zip` path!
```

#### Defining an area

`bbox` is the only required parameter for the `Landfire` class. It must be a string and have form `min_x min_y max_x max_y`. For example, `-107.70894965 46.56799094 -106.02718124 47.34869094`.

#### Resampling data

If you'd like to resample your results, use the parameter `resample_res`, specifying the grid resolution (in meters) of interest. The default value is 30 meters and may go as high as 9999 meters. Requesting a finer resolution than 30 m will return an error.

#### Reprojecting data

You may specify a different output coordinate reference system by providing the well-known ID to `output_crs`. This parameter defaults to `none`, preserving the output CRS from LANDFIRE for compatability with fire modeling applications. If not using this data for models like FlamMap, FARSITE, etc., we recommend specifying an `output_crs` of `4326` for WGS84 or `3857` for WGS84 Web-Mercator.

### Downloading data

With your `Landfire` class initialized, all that is left is to call `request_data()` for your layers of interest. You must provide a list of layers and an output path to successfully download data. Here we use the `ProductSearch` class to find the layer list for us.

```python
import landfire
from landfire.product.enums import ProductVersion
from landfire.product.search import ProductSearch

landfire.Landfire(bbox="-107.70894965 46.56799094 -106.02718124 47.34869094").request_data(
        layers=ProductSearch(
                names=["succession classes"],
                versions=[ProductVersion.lf_2020],
                ).get_layers(),
        output_path="./test.zip"
)
```

#### Specifying an output path

A path-like string representing where the output should be saved. The path needs to exist but the file name does not. The file name must end in `.zip`.

#### Monitoring your request status status output

During the download process your request will go through several steps involving raster processes that can take a bit of time. We poll the LANDFIRE processing API with a linear strategy, requesting updates every 5, 10, 15, ... seconds (default update interval) until the data is downloaded. The status of your data request, time until next update, and a progress bar are displayed in the console so you can monitor your request.

If you'd like to suppress this output, set `show_status=False`. If you would like to change the interval at which you receive status updates, change `backoff_base_value`. For example, specifying a backoff base value of `10` will query the API every 10, 20, 30, ... seconds. Please be courteous with this parameter as it will directly affect the number of calls to the LANDFIRE API!
