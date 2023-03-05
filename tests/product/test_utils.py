"""Product utilities tests."""
from landfire.product.utils import (
    get_product_codes,
    get_product_names,
    get_product_regions,
    get_product_themes,
    get_product_version_mapping,
    get_product_versions,
)


def test_get_product_names() -> None:
    """Test get_product_names() produces a list of product names."""
    names = get_product_names()
    assert isinstance(names, list)
    assert len(names) == 76


def test_get_product_codes() -> None:
    """Test get_product_codes() produces a list of product codes."""
    codes = get_product_codes()
    assert isinstance(codes, list)
    assert len(codes) == 76


def test_get_product_themes() -> None:
    """Test get_product_themes() produces a list of product themes."""
    themes = get_product_themes()
    assert themes == [
        "disturbance",
        "fire_regime",
        "fuel",
        "topographic",
        "transportation",
        "vegetation",
        "mod_fis",
        "map_zones",
    ]


def test_get_product_versions() -> None:
    """Test get_product_versions() produces a list of product versions."""
    versions = get_product_versions()
    assert versions == [
        "lf_2001",
        "lf_2012",
        "lf_2014",
        "lf_2016_remap",
        "lf_2020",
    ]


def test_get_product_version_mapping() -> None:
    """Test get_product_version_mapping() produces a Dict of product versions and values."""
    versions = get_product_version_mapping()
    assert versions == {
        "lf_2001": "1.0.5",
        "lf_2012": "1.3.0",
        "lf_2014": "1.4.0",
        "lf_2016_remap": "2.0.0",
        "lf_2020": "2.2.0",
    }


def test_get_product_regions() -> None:
    """Test get_product_regions() produces a list of product regions."""
    regions = get_product_regions()
    assert regions == ["US", "AK", "HI"]
