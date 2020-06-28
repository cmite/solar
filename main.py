from enum import Enum
from random import randrange
from bokeh.plotting import figure, output_file, show
from bokeh.models import Circle, Label
import json
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

    # Define plot
    output_file("solar-system.html")
    p = figure(title="Solar system", x_axis_label='x', y_axis_label='y', background_fill_color='black')
    p.xgrid.visible = False
    p.ygrid.visible = False
    p.sizing_mode = 'scale_width'
    
    # Sun
    sun = Star(name="Sun", position=(0., 0.), radius=696342.0)
    p.circle(x=sun.position[0], y=sun.position[1], radius=sun.radius, fill_color="yellow")

    # Planets
    solar_system = json.load(open("data/solar.json", 'r'))
    solar_planets = solar_system.get("planets", [])
    planets = []
    for planet in solar_planets:
        planets.append(
            Planet(
                name=planet.get("name"),
                orbit=Orbit(a=planet.get("a"), e=planet.get("e"), center=sun.position),
                radius=planet.get("radius"),
                color=planet.get("color")
            )
        )

    # Moons
    solar_moons = solar_system.get("moons", [])
    moons = []
    for moon in solar_moons:
        moons.append(
            Moon(
                name=moon.get("name"),
                orbit=Orbit(a=moon.get("a"), e=moon.get("e"), center=planets[SolarPosition[moon["planet"]].value].position()),
                radius=moon.get("radius"),
                color=moon.get("color")
            )
        )

    for planet in planets:
        draw_orbit(p, planet)

    for moon in moons:
        draw_orbit(p, moon)

    show(p)
