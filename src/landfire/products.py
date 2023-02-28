"""Product models."""
from typing import List
from typing import Optional

from pydantic import BaseModel

from landfire.enums import ProductRegion
from landfire.enums import ProductTheme
from landfire.enums import ProductVersion


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
    availability: Optional[List[ProductAvailability]]


products: List[Product] = [
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
        availability=None,
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
]
