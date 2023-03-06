"""Search class for obtaining product information."""
from typing import List, Optional

from attr import define, field

from landfire.product.enums import ProductRegion, ProductTheme, ProductVersion
from landfire.product.models import PRODUCTS, Product


@define
class ProductSearch:
    """Facilitates the search of possible LANDFIRE products to download."""

    _products: List[Product] = field(default=PRODUCTS, init=False)

    def __filter_by_name(self, names: List[str]) -> None:
        """Filter products by name(s).

        Args:
            names: List of product names to filter product list by.
        """
        self._products = [
            product
            for product in self._products
            if product.name in [name.lower() for name in names]
        ]

    def __filter_by_code(self, codes: List[str]) -> None:
        """Filter products by product code(s).

        Args:
            codes: List of product codes to filter product list by.
        """
        self._products = [
            product
            for product in self._products
            if product.code in [code for code in codes]
        ]

    def __filter_by_theme(self, themes: List[ProductTheme]) -> None:
        """Filter products by product theme(s).

        Args:
            themes: List of ProductThemes to filter product list by.
        """
        self._products = [
            product for product in self._products if product.theme in themes
        ]

    def __filter_by_version(self, versions: List[ProductVersion]) -> None:
        """Filter products by product version.

        Args:
            versions: List of ProductVersions to filter product list by.
        """
        products = []
        for product in self._products:
            for pa in product.availability:
                if any(v == pa.version for v in versions):
                    products.append(product)
        self._products = products

    def __filter_by_region(self, regions: List[ProductRegion]) -> None:
        """Filter products by product region. Do I like this? No. Does it work? Yes.

        Args:
            regions: List of ProductRegions to filter product list by.
        """
        products = []
        for product in self._products:
            for pa in product.availability:
                if bool(set(regions).intersection(pa.regions)):
                    products.append(product)
                    break
        self._products = products

    def __get_final_layers(self) -> List[str]:
        """Get list of layers from list of Products remaining."""
        layers: List[str] = []
        # Remaining products
        for product in self._products:
            # Availability in product
            for pa in product.availability:
                for layer in pa.layers:
                    layers.append(layer)
        # Convert to set to remove duplicates (map_zone, disturbances) that are present across each version. Landfire API has no way of specifying which version to use for these.
        return list(set(layers))

    def search_products(
        self,
        *,
        names: Optional[List[str]] = None,
        codes: Optional[List[str]] = None,
        themes: Optional[List[ProductTheme]] = None,
        versions: Optional[List[ProductVersion]] = None,
        regions: Optional[List[ProductRegion]] = None,
    ) -> List[Product]:
        """Search products for a particular combination of names, product codes, themes, versions, and regions. Passing no arguments results in all products being returned.

        Args:
            names: Product names.
            codes: Product codes.
            themes: Product themes. See ProductTheme enum.
            versions: Product versions. See ProductVersion enum.
            regions: Product regions. See ProductRegion enum.

        Returns:
            List of matching Products.
        """
        if names:
            self.__filter_by_name(names)
        if codes:
            self.__filter_by_code(codes)
        if themes:
            self.__filter_by_theme(themes)
        if versions:
            self.__filter_by_version(versions)
        if regions:
            self.__filter_by_region(regions)

        return self._products

    def get_layers(self) -> List[str]:
        """Get a list of layers corresponding to final, filtered list of Products."""
        return self.__get_final_layers()
