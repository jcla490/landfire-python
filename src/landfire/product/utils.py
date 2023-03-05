"""Product utilities. Mostly for user convenience."""
from typing import Dict, List

from landfire.product.enums import ProductRegion, ProductTheme, ProductVersion
from landfire.product.models import PRODUCTS


def get_product_names() -> List[str]:
    """Get a list of all possible LANDFIRE product names."""
    return [product.name for product in PRODUCTS]


def get_product_codes() -> List[str]:
    """Get a list of all possible LANDFIRE product codes."""
    return [product.code for product in PRODUCTS]


def get_product_themes() -> List[str]:
    """Get a list of all possible LANDFIRE ProductTheme enum members."""
    return [member.name for member in ProductTheme]


def get_product_versions() -> List[str]:
    """Get a list of all possible LANDFIRE ProductVersions enum members."""
    return [member.name for member in ProductVersion]


def get_product_version_mapping() -> Dict[str, str]:
    """Get a dict of all possible LANDFIRE ProductVersions enum members and values.

    This is useful if you're having trouble remembering which LANDFIRE version corresponds to which year release.
    """
    return {member.name: member.value for member in ProductVersion}


def get_product_regions() -> List[str]:
    """Get a list of all possible LANDFIRE ProductRegions enum members."""
    return [member.name for member in ProductRegion]
