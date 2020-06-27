from typing import Tuple


class Star:
    """Star class."""

    def __init__(self, name: str, center: Tuple[float, float], radius: float):
        self.center = center
        self.name = name
        self.radius = radius
