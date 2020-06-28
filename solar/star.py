from typing import Tuple


class Star:
    """Star class."""

    def __init__(self, name: str, position: Tuple[float, float], radius: float):
        self.position = position
        self.name = name
        self.radius = radius
