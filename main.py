from matplotlib import pyplot as plt
from random import randrange

from solar.orbit import Orbit
from solar.planet import Planet
from solar.star import Star


if __name__ == "__main__":
    k_km = 1000.0
    m_km = 1000000.0
    scaling = 100.0

    sun = Star(name="Sun", center=(0., 0.), radius=1.3927*m_km)
    sun_circle = plt.Circle(sun.center, radius=sun.radius, color='yellow')
    plt.gca().add_artist(sun_circle)

    planets = [
        Planet(
            name="Mercury",
            orbit=Orbit(a=57.9*m_km, e=0.20564),
            radius=4.879*k_km,
            color='brown'
        ),
        Planet(
            name="Venus",
            orbit=Orbit(a=108.2*m_km, e=0.00678),
            radius=12.104*k_km,
            color='pink'
        ),
        Planet(
            name="Earth",
            orbit=Orbit(a=152.0*m_km, e=0.01671123),
            radius=12.742*k_km,
            color='blue'
        ),
        Planet(
            name="Mars",
            orbit=Orbit(a=228.0*m_km, e=0.09339),
            radius=6.779*k_km,
            color='red'
        ),
        Planet(
            name="Jupiter",
            orbit=Orbit(a=778.3*m_km, e=0.04939),
            radius=139.820*k_km,
            color='orange'
        ),
        Planet(
            name="Saturn",
            orbit=Orbit(a=1426.7*m_km, e=0.0539),
            radius=116.460*k_km,
            color='yellow'
        ),
        Planet(
            name="Uranus",
            orbit=Orbit(a=2870.7*m_km, e=0.04726),
            radius=50.724*k_km,
            color='blue'
        ),
        Planet(
            name="Neptune",
            orbit=Orbit(a=4498.4*m_km, e=0.00859),
            radius=49.244*k_km,
            color='navy'
        ),
        
    ]

    for planet in planets:
        ellipse = planet.elliptic_orbit()
        plt.plot(
            sun.center[0] + ellipse[0, :],
            sun.center[1] + ellipse[1, :],
            linewidth=0.05,
            color='white'
        )
        r = randrange(len(ellipse[0, :]))
        circle = plt.Circle(
            (ellipse[0, r], ellipse[1, r]),
            radius=planet.radius*scaling,
            color=planet.color
        )
        plt.gca().add_artist(circle)
        plt.gca().annotate(
            planet.name,
            xy=(ellipse[0, r], ellipse[1, r]),
            fontsize=7,
            ha='center',
            color='white'
        )

    plt.gca().set_facecolor('xkcd:dark')
    plt.show()
