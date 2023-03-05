"""Product enumerations."""

from enum import Enum


class ProductTheme(str, Enum):
    """Product themes."""

    disturbance = "disturbance"
    fire_regime = "fire regime"
    fuel = "fuel"
    topographic = "topographic"
    transportation = "transportation"
    vegetation = "vegetation"
    mod_fis = "mod-fis"
    map_zones = "map zones"


class ProductRegion(str, Enum):
    """Product availability regions."""

    US = "US"
    AK = "AK"
    HI = "HI"


class ProductVersion(str, Enum):
    """Product versions."""

    lf_2001 = "1.0.5"
    lf_2012 = "1.3.0"
    lf_2014 = "1.4.0"
    lf_2016_remap = "2.0.0"
    lf_2020 = "2.2.0"
