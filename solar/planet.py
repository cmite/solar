from solar.orbit import Orbit


class Planet:
    """Planet class."""

    def __init__(self, name: str, orbit: Orbit, radius: float, color: str = "white"):
        self.name = name
        self.orbit = orbit
        self.radius = radius
        self.color = color

    def elliptic_orbit(self):
        """Returns the elliptic orbit."""
        return self.orbit.ellipse()
