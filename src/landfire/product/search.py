"""Search class for obtaining product information."""
from typing import List, Optional

from attr import define, field

from landfire.product.enums import ProductRegion, ProductTheme, ProductVersion
from landfire.product.models import PRODUCTS, Product


@define
class ProductSearch:
    """Search object to find available LANDFIRE products given a particular combination of names, product codes, themes, versions, and regions.

    Call get_products() or get_layers() to get search output depending on your needs. Passing no arguments to this class will result in no actual searching and methods called on this object will return all products/layers.

    Args:
        names: Product names.
        codes: Product codes.
        themes: Product themes. See ProductTheme enum.
        versions: Product versions. See ProductVersion enum.
        regions: Product regions. See ProductRegion enum.

    """

    names: Optional[List[str]] = field(kw_only=True, default=None)
    codes: Optional[List[str]] = field(kw_only=True, default=None)
    themes: Optional[List[ProductTheme]] = field(kw_only=True, default=None)
    versions: Optional[List[ProductVersion]] = field(kw_only=True, default=None)
    regions: Optional[List[ProductRegion]] = field(kw_only=True, default=None)

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

    def __get_layers(self, products: List[Product]) -> List[str]:
        """Get list of layers from list of Products."""
        layers: List[str] = []
        for product in products:
            # Availability in product
            for pa in product.availability:
                for layer in pa.layers:
                    layers.append(layer)
        # Convert to set to remove duplicates (map_zone, disturbances) that are present across each version. Landfire API has no way of specifying which version to use for these.
        return list(set(layers))

    def __query(
        self,
        *,
        names: Optional[List[str]] = None,
        codes: Optional[List[str]] = None,
        themes: Optional[List[ProductTheme]] = None,
        versions: Optional[List[ProductVersion]] = None,
        regions: Optional[List[ProductRegion]] = None,
    ) -> List[Product]:
        """Query products for a particular combination of names, product codes, themes, versions, and regions. Passing no arguments results in no actual searching.

        Args:
            names: Product names.
            codes: Product codes.
            themes: Product themes. See ProductTheme enum.
            versions: Product versions. See ProductVersion enum.
            regions: Product regions. See ProductRegion enum.

        Returns:
            List of matching products.
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

    def get_products(self) -> List[Product]:
        """Get a list of matching Products from ProductSearch.

        Returns:
            List of Products.
        """
        return self.__query(
            names=self.names,
            codes=self.codes,
            themes=self.themes,
            versions=self.versions,
            regions=self.regions,
        )

    def get_layers(self) -> List[str]:
        """Get a list of matching layers from ProductSearch.

        Returns:
            List of product layers.
        """
        products = self.__query(
            names=self.names,
            codes=self.codes,
            themes=self.themes,
            versions=self.versions,
            regions=self.regions,
        )
        return self.__get_layers(products)
