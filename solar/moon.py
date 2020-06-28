from random import randrange
from solar.orbit import Orbit


class Moon:
    """Define Moons."""

    def __init__(self, name: str, orbit: Orbit, radius: float, color: str):
        self.name = name
        self.radius = radius
        self.orbit = orbit
        self.color = color
        self.random_index = randrange(100)


    def elliptic_orbit(self):
        """Returns the elliptic orbit."""
        return self.orbit.ellipse()

    def position(self):
        """Returns the planet's position."""
        trajectory = self.elliptic_orbit()
        return trajectory[0, self.random_index], trajectory[1, self.random_index]

    def orbital_center(self):
        """Returns the center of the orbit."""
        return self.orbit.center
