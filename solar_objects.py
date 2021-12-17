# coding: utf-8
# license: GPLv3


class Star:
    """Datatype for star specification. 
    Records star's mass, coordinates, radius in pixels, colour.
    """

    type = "star"
    """object type"""

    m = 0
    """mass"""

    x = 0
    """x coordinate"""

    y = 0
    """y coordinate"""

    Vx = 0
    """velocity, x component"""

    Vy = 0
    """velocity, y component"""

    Fx = 0
    """force, x component"""

    Fy = 0
    """force, y component"""

    R = 5
    """radius"""

    color = "red"
    """colour"""

    image = None
    """star's picture (tkinter)"""


class Planet:
    """Datatype for planet specification. 
    Records planet's mass, coordinates, radius in pixels, colour.
    
    """

    type = "planet"
    """object type"""

    m = 0
    """mass"""

    x = 0
    """x coordinate"""

    y = 0
    """y coordinate"""

    Vx = 0
    """velocity, x component"""

    Vy = 0
    """velocity, y component"""

    Fx = 0
    """force, x component"""

    Fy = 0
    """force, y component"""

    R = 5
    """radius"""

    color = "green"
    """colour"""

    image = None
    """planet's picture (tkinter)"""
