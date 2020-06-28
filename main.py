from enum import Enum
from random import randrange
from bokeh.plotting import figure, output_file, show
from bokeh.models import Circle, Label

from solar.orbit import Orbit
from solar.planet import Planet
from solar.star import Star
from solar.moon import Moon


class SolarPosition(Enum):
    MERCURY = 0
    VENUS = 1
    EARTH = 2
    MARS = 3
    JUPITER = 4
    SATURN = 5
    URANUS = 6
    NEPTUNE = 7
    PLUTO = 8


def draw_orbit(fig, stellar_object):
    ellipse = stellar_object.elliptic_orbit()
    center = stellar_object.orbital_center()
    position = stellar_object.position()

    fig.line(center[0] + ellipse[0, :], center[1] + ellipse[1, :], line_width=0.5, line_color='white')
    fig.circle(x=center[0] + position[0], y=center[1] + position[1], radius=stellar_object.radius, fill_color=stellar_object.color)
    mytext = Label(x=center[0] + position[0], y=center[1] + position[1], text=stellar_object.name, text_color='white')
    fig.add_layout(mytext)


if __name__ == "__main__":
    k_km = 1000.0
    m_km = 1000000.0

    # Define plot
    output_file("solar-system.html")
    p = figure(title="Solar system", x_axis_label='x', y_axis_label='y', background_fill_color='black')
    p.xgrid.visible = False
    p.ygrid.visible = False
    p.sizing_mode = 'scale_width'
    
    # Sun
    sun = Star(name="Sun", position=(0., 0.), radius=696.342*k_km)
    p.circle(x=sun.position[0], y=sun.position[1], radius=sun.radius, fill_color="yellow")

    # Planets
    planets = [
        Planet(
            name="Mercury",
            orbit=Orbit(a=57.9*m_km, e=0.20564, center=sun.position),
            radius=2.4397*k_km,
            color='brown'
        ),
        Planet(
            name="Venus",
            orbit=Orbit(a=108.2*m_km, e=0.00678, center=sun.position),
            radius=6.0518*k_km,
            color='pink'
        ),
        Planet(
            name="Earth",
            orbit=Orbit(a=152.0*m_km, e=0.01671123, center=sun.position),
            radius=6.378137*k_km,
            color='blue'
        ),
        Planet(
            name="Mars",
            orbit=Orbit(a=228.0*m_km, e=0.09339, center=sun.position),
            radius=3.3962*k_km,
            color='red'
        ),
        Planet(
            name="Jupiter",
            orbit=Orbit(a=778.3*m_km, e=0.04939, center=sun.position),
            radius=71.492*k_km,
            color='orange'
        ),
        Planet(
            name="Saturn",
            orbit=Orbit(a=1426.7*m_km, e=0.0539, center=sun.position),
            radius=60.268*k_km,
            color='yellow'
        ),
        Planet(
            name="Uranus",
            orbit=Orbit(a=2870.7*m_km, e=0.04726, center=sun.position),
            radius=25.559*k_km,
            color='blue'
        ),
        Planet(
            name="Neptune",
            orbit=Orbit(a=4498.4*m_km, e=0.00859, center=sun.position),
            radius=24.764*k_km,
            color='navy'
        ),
        Planet(
            name="Pluto",
            orbit=Orbit(a=5900.9*m_km, e=0.25024871, center=sun.position),
            radius=1.185*k_km,
            color='palegoldenrod'
        )
    ]

    # Moons
    moons = [
        Moon(
            name="Phobos",
            orbit=Orbit(a=9.377*k_km, e=0.015, center=planets[SolarPosition.MARS.value].position()),
            radius=11.267,
            color='grey'
        ),
        Moon(
            name="Deimos",
            orbit=Orbit(a=23.460*k_km, e=0.00033, center=planets[SolarPosition.MARS.value].position()),
            radius=6.2,
            color='grey'
        ),
        Moon(
            name="Moon",
            orbit=Orbit(a=384.748*k_km, e=0.0549, center=planets[SolarPosition.EARTH.value].position()),
            radius=1.7374*k_km,
            color='grey'
        ),
        Moon(
            name="Triton",
            orbit=Orbit(a=354.759*k_km, e=0.000016, center=planets[SolarPosition.NEPTUNE.value].position()),
            radius=1.353*k_km,
            color='grey'
        ),
        Moon(
            name="Nereid",
            orbit=Orbit(a=5513.4*k_km, e=0.7417482, center=planets[SolarPosition.NEPTUNE.value].position()),
            radius=178.5,
            color='grey'
        )
    ]

    for planet in planets:
        draw_orbit(p, planet)

    for moon in moons:
        draw_orbit(p, moon)

    show(p)
