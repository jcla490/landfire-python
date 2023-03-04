"""Search class for obtaining product layers."""
from typing import List, Optional

from landfire.enums import ProductRegion, ProductTheme, ProductVersion
from landfire.products import PRODUCTS, Product


class ProductSearch:
    """Product Search."""

    products = PRODUCTS

    def __filter_by_name(self, name: List[str]) -> None:
        """Filter products by name(s)."""
        self._products = [
            product
            for product in self.products
            if product.name in [name.lower() for name in name]
        ]

    def __filter_by_code(self, code: List[str]) -> None:
        """Filter products by product code(s)."""
        self._products = [
            product
            for product in self.products
            if product.code in [code.lower() for code in code]
        ]

    def __filter_by_theme(self, theme: List[ProductTheme]) -> None:
        """Filter products by product theme(s)."""
        self._products = [
            product for product in self.products if product.theme in theme
        ]

    def __filter_by_version(self, version: ProductVersion) -> None:
        """Filter products by product version."""
        self._products = [
            product for product in self.products if product.version == version
        ]

    def __filter_by_region(self, region: ProductRegion) -> None:
        """Filter products by product region."""
        self._products = [
            product for product in self.products if product.region == region
        ]

    def __get_final_layers(self) -> List[str]:
        """Get layers from list of Products remaining."""
        layers: List[str] = []
        # Remaining products
        for product in self._products:
            # Availability in product
            for pa in product.availability:
                # Some products have no availability
                if pa is not None:
                    for layer in pa.layers:
                        layers.append(layer)
        return layers

    def search_products(
        self,
        *,
        name: Optional[List[str]],
        code: Optional[List[str]],
        theme: Optional[List[ProductTheme]],
        version: Optional[List[ProductVersion]],
        region: Optional[List[ProductRegion]]
    ) -> List[Product]:
        """Search products."""
        if name:
            self.__filter_by_name(name)
        if code:
            self.__filter_by_code(code)
        if theme:
            self.__filter_by_theme(theme)
        if version:
            self.__filter_by_version(version)
        if region:
            self.__filter_by_region(region)

        return self.products

    def get_layers(self) -> List[str]:
        """Get layers from search query."""
        return self.__get_final_layers()
