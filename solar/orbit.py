from typing import Tuple
import numpy as np
from math import sqrt
from math import pi


class Orbit:
    """Planet orbit trajectory class."""

    def __init__(self, a: float, e: float, center: Tuple[float, float]):
        self.a = a
        self.e = e
        self.b = a * sqrt(1 - e*e)
        self.center = center

    def ellipse(self):
        """Elliptic orbit."""
        t = np.linspace(0, 2*pi, 100)
        return np.array([self.a * np.cos(t), self.b * np.sin(t)])
