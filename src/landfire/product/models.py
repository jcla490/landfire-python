"""Product models.

Adopted from https://lfps.usgs.gov/helpdocs/productstable.html.
"""
from typing import List

from pydantic import BaseModel

from landfire.product.enums import ProductRegion, ProductTheme, ProductVersion


class ProductAvailability(BaseModel):
    """Product Availability model with geographic regions corresponding to a particular version.

    Args:
        version: product version.
        regions: list of product regions.
        layers: list of product layers available.
    """

    version: ProductVersion
    regions: List[ProductRegion]
    layers: List[str]

    class Config:
        """Pydantic model config."""

        allow_mutation = False


class Product(BaseModel):
    """Product model.

    Args:
        name: name of the product.
        code: Landfire code of the product.
        theme: product theme.
        availability: list of ProductAvailability models containing information on versions and regions available.
    """

    name: str
    code: str
    theme: ProductTheme
    availability: List[ProductAvailability]

    class Config:
        """Pydantic model config."""

        allow_mutation = False


PRODUCTS: List[Product] = [
    Product(
        name="disturbance",
        code="DistYear",
        theme=ProductTheme.disturbance,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK],
                layers=[
                    "DIST1999",
                    "DIST2000",
                    "DIST2001",
                    "DIST2002",
                    "DIST2003",
                    "DIST2004",
                    "DIST2005",
                    "DIST2006",
                    "DIST2007",
                    "DIST2008",
                    "DIST2009",
                    "DIST2010",
                    "DIST2011",
                    "DIST2012",
                    "DIST2013",
                    "DIST2014",
                    "DIST2015",
                    "DIST2016",
                    "DIST2017",
                    "DIST2018",
                    "DIST2019",
                    "DIST2020",
                ],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=[
                    "DIST1999",
                    "DIST2000",
                    "DIST2001",
                    "DIST2002",
                    "DIST2003",
                    "DIST2004",
                    "DIST2005",
                    "DIST2006",
                    "DIST2007",
                    "DIST2008",
                    "DIST2009",
                    "DIST2010",
                    "DIST2011",
                    "DIST2012",
                    "DIST2013",
                    "DIST2014",
                    "DIST2015",
                    "DIST2016",
                    "DIST2017",
                    "DIST2018",
                    "DIST2019",
                    "DIST2020",
                ],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=[
                    "DIST1999",
                    "DIST2000",
                    "DIST2001",
                    "DIST2002",
                    "DIST2003",
                    "DIST2004",
                    "DIST2005",
                    "DIST2006",
                    "DIST2007",
                    "DIST2008",
                    "DIST2009",
                    "DIST2010",
                    "DIST2011",
                    "DIST2012",
                    "DIST2013",
                    "DIST2014",
                    "DIST2015",
                    "DIST2016",
                    "DIST2017",
                    "DIST2018",
                    "DIST2019",
                    "DIST2020",
                ],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=[
                    "DIST1999",
                    "DIST2000",
                    "DIST2001",
                    "DIST2002",
                    "DIST2003",
                    "DIST2004",
                    "DIST2005",
                    "DIST2006",
                    "DIST2007",
                    "DIST2008",
                    "DIST2009",
                    "DIST2010",
                    "DIST2011",
                    "DIST2012",
                    "DIST2013",
                    "DIST2014",
                    "DIST2015",
                    "DIST2016",
                    "DIST2017",
                    "DIST2018",
                    "DIST2019",
                    "DIST2020",
                ],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=[
                    "DIST1999",
                    "DIST2000",
                    "DIST2001",
                    "DIST2002",
                    "DIST2003",
                    "DIST2004",
                    "DIST2005",
                    "DIST2006",
                    "DIST2007",
                    "DIST2008",
                    "DIST2009",
                    "DIST2010",
                    "DIST2011",
                    "DIST2012",
                    "DIST2013",
                    "DIST2014",
                    "DIST2015",
                    "DIST2016",
                    "DIST2017",
                    "DIST2018",
                    "DIST2019",
                    "DIST2020",
                ],
            ),
        ],
    ),
    Product(
        name="fuel disturbance",
        code="FDistYear",
        theme=ProductTheme.disturbance,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["FDIST2012"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["FDIST2014"],
            ),
        ],
    ),
    Product(
        name="fuel disturbance 2019",
        code="FDistYear",
        theme=ProductTheme.disturbance,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US],
                layers=["FDIST2019"],
            ),
        ],
    ),
    Product(
        name="fuel disturbance 2020",
        code="FDistYear",
        theme=ProductTheme.disturbance,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["FDIST2020"],
            ),
        ],
    ),
    Product(
        name="fuel disturbance 2021",
        code="FDistYear",
        theme=ProductTheme.disturbance,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["FDIST2021"],
            ),
        ],
    ),
    Product(
        name="fuel disturbance 2022",
        code="FDist",
        theme=ProductTheme.disturbance,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["FDIST2022"],
            ),
        ],
    ),
    Product(
        name="historical disturbance",
        code="HDist",
        theme=ProductTheme.disturbance,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["HDIST2016"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["HDIST2020"],
            ),
        ],
    ),
    Product(
        name="fire regime groups",
        code="FRG",
        theme=ProductTheme.fire_regime,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105FRG"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130FRG"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140FRG"],
            ),
        ],
    ),
    Product(
        name="mean fire return interval",
        code="MFRI",
        theme=ProductTheme.fire_regime,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.AK, ProductRegion.HI],
                layers=["105MFRI"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130MFRI"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140MFRI"],
            ),
        ],
    ),
    Product(
        name="percent low-severity fire",
        code="PLS",
        theme=ProductTheme.fire_regime,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105PLS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130PLS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140PLS"],
            ),
        ],
    ),
    Product(
        name="percent mixed-severity fire",
        code="PMS",
        theme=ProductTheme.fire_regime,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105PMS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130PMS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140PMS"],
            ),
        ],
    ),
    Product(
        name="percent replacement-severity fire",
        code="PRS",
        theme=ProductTheme.fire_regime,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105PLS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130PLS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140PLS"],
            ),
        ],
    ),
    Product(
        name="succession classes",
        code="SClass",
        theme=ProductTheme.fire_regime,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105SCLASS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130SCLASS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140SCLASS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.HI],
                layers=["200SCLASS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.HI],
                layers=["220SCLASS"],
            ),
        ],
    ),
    Product(
        name="vegetation condition class",
        code="VCC",
        theme=ProductTheme.fire_regime,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105VCC"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130VCC"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140VCC"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.HI],
                layers=["200VCC"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.HI],
                layers=["220VCC"],
            ),
        ],
    ),
    Product(
        name="vegetation departure index",
        code="VDep",
        theme=ProductTheme.fire_regime,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105VDEP"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130VDEP"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140VDEP"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.HI],
                layers=["200VDEP"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.HI],
                layers=["220VDEP"],
            ),
        ],
    ),
    Product(
        name="13 anderson fire behavior fuel models",
        code="FBFM13",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105FBFM13"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130FBFM13"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140FBFM13"],
            ),
        ],
    ),
    Product(
        name="13 anderson fire behavior fuel models 2019",
        code="FBFM13",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US],
                layers=["200F13_19"],
            ),
        ],
    ),
    Product(
        name="13 anderson fire behavior fuel models 2020",
        code="FBFM13",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["200F13_20"],
            ),
        ],
    ),
    Product(
        name="13 anderson fire behavior fuel models 2022",
        code="FBFM13",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["220F13_22"],
            ),
        ],
    ),
    Product(
        name="40 scott and burgan fire behavior fuel models",
        code="FBFM40",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105FBFM40"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130FBFM40"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140FBFM40"],
            ),
        ],
    ),
    Product(
        name="40 scott and burgan fire behavior fuel models 2019",
        code="FBFM40",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US],
                layers=["200F40_19"],
            ),
        ],
    ),
    Product(
        name="40 scott and burgan fire behavior fuel models 2020",
        code="FBFM40",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["200F40_20"],
            ),
        ],
    ),
    Product(
        name="40 scott and burgan fire behavior fuel models 2022",
        code="FBFM40",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["220F40_22"],
            ),
        ],
    ),
    Product(
        name="canadian forest fire danger rating system",
        code="CFFDRS",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.AK],
                layers=["105CFFDRS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.AK],
                layers=["130CFFDRS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.AK],
                layers=["140CFFDRS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.AK],
                layers=["200CFFDRS"],
            ),
        ],
    ),
    Product(
        name="canadian forest fire danger rating system 2022",
        code="CFFDRS",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.AK],
                layers=["220CFFDRS"],
            ),
        ],
    ),
    Product(
        name="forest canopy base height",
        code="CBH",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105FBFM40"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130FBFM40"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140FBFM40"],
            ),
        ],
    ),
    Product(
        name="forest canopy base height 2019",
        code="CBH",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US],
                layers=["200CBH_19"],
            ),
        ],
    ),
    Product(
        name="forest canopy base height 2020",
        code="CBH",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["200CBH_20"],
            ),
        ],
    ),
    Product(
        name="forest canopy base height 2022",
        code="CBH",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["220CBH_22"],
            ),
        ],
    ),
    Product(
        name="forest canopy bulk density",
        code="CBD",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105CBD"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130CBD"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140CBD"],
            ),
        ],
    ),
    Product(
        name="forest canopy bulk density 2019",
        code="CBD",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US],
                layers=["200CBD_19"],
            ),
        ],
    ),
    Product(
        name="forest canopy bulk density 2020",
        code="CBD",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["200CBD_20"],
            ),
        ],
    ),
    Product(
        name="forest canopy bulk density 2022",
        code="CBD",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["220CBD_22"],
            ),
        ],
    ),
    Product(
        name="forest canopy cover",
        code="CC",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105CC"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130CC"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140CC"],
            ),
        ],
    ),
    Product(
        name="forest canopy cover 2019",
        code="CC",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US],
                layers=["200CC_19"],
            ),
        ],
    ),
    Product(
        name="forest canopy cover 2020",
        code="CC",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["200CC_20"],
            ),
        ],
    ),
    Product(
        name="forest canopy cover 2022",
        code="CC",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["220CC_22"],
            ),
        ],
    ),
    Product(
        name="forest canopy height",
        code="CH",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105CH"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130CH"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140CH"],
            ),
        ],
    ),
    Product(
        name="forest canopy height 2019",
        code="CH",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US],
                layers=["200CH_19"],
            ),
        ],
    ),
    Product(
        name="forest canopy height 2020",
        code="CH",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["200CH_20"],
            ),
        ],
    ),
    Product(
        name="forest canopy height 2022",
        code="CH",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["220CH_22"],
            ),
        ],
    ),
    Product(
        name="fuel characteristic classification system fuelbeds",
        code="FCCS",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105FCCS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140FCCS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["200FCCS20"],
            ),
        ],
    ),
    Product(
        name="fuel characteristic classification system fuelbeds 2022",
        code="FCCS",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["220FCCS22"],
            ),
        ],
    ),
    Product(
        name="fuel vegetation cover 2019",
        code="FVC",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US],
                layers=["200FVC_19"],
            ),
        ],
    ),
    Product(
        name="fuel vegetation cover 2020",
        code="FVC",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["200FVC_20"],
            ),
        ],
    ),
    Product(
        name="fuel vegetation cover 2022",
        code="FVC",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["220FVC_22"],
            ),
        ],
    ),
    Product(
        name="fuel vegetation height 2019",
        code="FVH",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US],
                layers=["200FVH_19"],
            ),
        ],
    ),
    Product(
        name="fuel vegetation height 2020",
        code="FVH",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["200FVH_20"],
            ),
        ],
    ),
    Product(
        name="fuel vegetation height 2022",
        code="FVH",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["220FVH_22"],
            ),
        ],
    ),
    Product(
        name="fuel vegetation type 2019",
        code="FVT",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US],
                layers=["200FVT_19"],
            ),
        ],
    ),
    Product(
        name="fuel vegetation type 2020",
        code="FVC",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["200FVT_20"],
            ),
        ],
    ),
    Product(
        name="fuel vegetation type 2022",
        code="FVC",
        theme=ProductTheme.fuel,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["220FVT_22"],
            ),
        ],
    ),
    Product(
        name="aspect",
        code="ASP",
        theme=ProductTheme.topographic,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["ASP2020"],
            ),
        ],
    ),
    Product(
        name="elevation",
        code="ELEV",
        theme=ProductTheme.topographic,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["ELEV2020"],
            ),
        ],
    ),
    Product(
        name="slope degrees",
        code="SLPD",
        theme=ProductTheme.topographic,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["SLPD2020"],
            ),
        ],
    ),
    Product(
        name="slope percent rise",
        code="SLPP",
        theme=ProductTheme.topographic,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["SLPP2020"],
            ),
        ],
    ),
    Product(
        name="operational roads",
        code="ROADS",
        theme=ProductTheme.transportation,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK],
                layers=["220ROADS_20"],
            ),
        ],
    ),
    Product(
        name="biophysical settings",
        code="BPS",
        theme=ProductTheme.vegetation,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105BPS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130BPS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140BPS"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.HI],
                layers=["200BPS"],
            ),
        ],
    ),
    Product(
        name="environmental site potential",
        code="ESP",
        theme=ProductTheme.vegetation,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105ESP"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130ESP"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140ESP"],
            ),
        ],
    ),
    Product(
        name="existing vegetation cover",
        code="EVC",
        theme=ProductTheme.vegetation,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105EVC"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130EVC"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140EVC"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["200EVC"],
            ),
        ],
    ),
    Product(
        name="existing vegetation cover 2022",
        code="EVC",
        theme=ProductTheme.vegetation,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["220EVC_22"],
            ),
        ],
    ),
    Product(
        name="existing vegetation height",
        code="EVH",
        theme=ProductTheme.vegetation,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105EVH"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130EVH"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140EVH"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["200EVH"],
            ),
        ],
    ),
    Product(
        name="existing vegetation height 2022",
        code="EVH",
        theme=ProductTheme.vegetation,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["220EVH_22"],
            ),
        ],
    ),
    Product(
        name="existing vegetation type",
        code="EVT",
        theme=ProductTheme.vegetation,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["105EVT"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["130EVT"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["140EVT"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["200EVT"],
            ),
        ],
    ),
    Product(
        name="existing vegetation cover 2020",
        code="EVT",
        theme=ProductTheme.vegetation,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["220EVT"],
            ),
        ],
    ),
    Product(
        name="national vegetation classification",
        code="NVC",
        theme=ProductTheme.vegetation,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["200NVC"],
            ),
        ],
    ),
    Product(
        name="mod-fis fuel vegetation cover (spring)",
        code="MF_FVC",
        theme=ProductTheme.mod_fis,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US],
                layers=["MF_FVCSP22"],
            ),
        ],
    ),
    Product(
        name="mod-fis fuel vegetation cover (summer)",
        code="MF_FVC",
        theme=ProductTheme.mod_fis,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US],
                layers=["MF_FVCSU22"],
            ),
        ],
    ),
    Product(
        name="mod-fis fuel vegetation cover (fall)",
        code="MF_FVC",
        theme=ProductTheme.mod_fis,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US],
                layers=["MF_FVCFA22"],
            ),
        ],
    ),
    Product(
        name="mod-fis fuel vegetation height (spring)",
        code="MF_FVH",
        theme=ProductTheme.mod_fis,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US],
                layers=["MF_FVHSP22"],
            ),
        ],
    ),
    Product(
        name="mod-fis fuel vegetation height (summer)",
        code="MF_FVH",
        theme=ProductTheme.mod_fis,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US],
                layers=["MF_FVHSU22"],
            ),
        ],
    ),
    Product(
        name="mod-fis fuel vegetation height (fall)",
        code="MF_FVH",
        theme=ProductTheme.mod_fis,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US],
                layers=["MF_FVHFA22"],
            ),
        ],
    ),
    Product(
        name="mod-fis fire behavior fuel model 40 (spring)",
        code="MF_F40",
        theme=ProductTheme.mod_fis,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US],
                layers=["MF_F40SP22"],
            ),
        ],
    ),
    Product(
        name="mod-fis fire behavior fuel model 40 (summer)",
        code="MF_F40",
        theme=ProductTheme.mod_fis,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US],
                layers=["MF_F40SU22"],
            ),
        ],
    ),
    Product(
        name="mod-fis fire behavior fuel model 40 (fall)",
        code="MF_F40",
        theme=ProductTheme.mod_fis,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US],
                layers=["MF_F40FA22"],
            ),
        ],
    ),
    Product(
        name="landfire map zones",
        code="map_zones",
        theme=ProductTheme.map_zones,
        availability=[
            ProductAvailability(
                version=ProductVersion.lf_2001,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["map_zones"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2012,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["map_zones"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2014,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["map_zones"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2016_remap,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["map_zones"],
            ),
            ProductAvailability(
                version=ProductVersion.lf_2020,
                regions=[ProductRegion.US, ProductRegion.AK, ProductRegion.HI],
                layers=["map_zones"],
            ),
        ],
    ),
]
