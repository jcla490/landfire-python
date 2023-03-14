"""ProductSearch tests."""
from landfire.product.enums import ProductRegion, ProductTheme, ProductVersion
from landfire.product.search import ProductSearch


PRODUCT_LIST_LEN = 76


def test_init_product_search() -> None:
    """Test ProductSearch() instantiates."""
    search = ProductSearch()
    assert isinstance(search, ProductSearch)


def test_search_products_no_params() -> None:
    """Test ProductSearch.get_products() uses no filters."""
    products = ProductSearch().get_products()
    assert len(products) == PRODUCT_LIST_LEN


def test_search_products_names() -> None:
    """Test ProductSearch.get_products() filters by name."""
    products = ProductSearch(
        names=["fuel vegetation cover 2020", "landfire map zones"]
    ).get_products()
    assert len(products) == 2


def test_search_products_codes() -> None:
    """Test ProductSearch.get_products() filters by code."""
    products = ProductSearch(codes=["FBFM40"]).get_products()
    assert len(products) == 4


def test_search_products_themes() -> None:
    """Test ProductSearch.get_products() filters by theme."""
    products = ProductSearch(
        themes=[ProductTheme.disturbance, ProductTheme.fuel]
    ).get_products()
    assert len(products) == 44


def test_search_products_versions() -> None:
    """Test ProductSearch.get_products() filters by version."""
    products = ProductSearch(versions=[ProductVersion.lf_2001]).get_products()
    assert len(products) == 23


def test_search_products_regions() -> None:
    """Test ProductSearch.get_products() filters by region."""
    products = ProductSearch(regions=[ProductRegion.HI]).get_products()
    assert len(products) == 54


def test_search_products_regions_two() -> None:
    """Test ProductSearch.get_products() filters by regions."""
    products = ProductSearch(
        regions=[ProductRegion.HI, ProductRegion.AK]
    ).get_products()
    assert len(products) == 57


def test_search_products_regions_three() -> None:
    """Test ProductSearch.get_products() filters by regions."""
    products = ProductSearch(
        regions=[ProductRegion.HI, ProductRegion.AK, ProductRegion.US]
    ).get_products()
    assert len(products) == PRODUCT_LIST_LEN


def test_search_products_combination() -> None:
    """Test ProductSearch.get_products() filters by several args."""
    products = ProductSearch(
        versions=[ProductVersion.lf_2001],
        themes=[ProductTheme.fire_regime],
        codes=["MFRI"],
        names=["mean fire return interval"],
    ).get_products()
    assert len(products) == 1


def test_search_products_get_layers() -> None:
    """Test ProductSearch.get_layers() returns filtered layers."""
    layers = ProductSearch(names=["disturbance"]).get_layers()
    assert len(layers) == 22
