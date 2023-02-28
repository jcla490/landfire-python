"""Landfire."""

from typing import List

from attrs import define


__version__ = "0.0.0"
__all__ = ["landfire"]


@define
class Landfire:
    """Accessor class for LANDFIRE."""

    bbox: List[float]


# CRS conversion helper?
# bounding box or file helper
# ready made layer lists for common workflows (i.e., flammap)
