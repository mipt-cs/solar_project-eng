# coding: utf-8
# license: GPLv3

"""Visualisation module. Object screen coordinates are used only in this module. 
"""

header_font = "Arial-16"
"""font in wondow header"""

window_width = 800
"""window width in pixels"""

window_height = 800
"""window height in pixels"""

scale_factor = None
"""coordinate scaling factor. For physical coordinates to screen coordinates transform. In pixels-per-metre.
type: float
"""


def calculate_scale_factor(max_distance):
    """calculates coordinate scale factor"""
    global scale_factor
    scale_factor = 0.4*min(window_height, window_width)/max_distance
    print('Scale factor:', scale_factor)


def scale_x(x):
    """Calculates screen **x** coordinate using model **x** coordinate.
    Takes float, returns integer.
    if the resulting **x** exceeds screen dimensions - the exceeding coordinate is returned.

    Parametres:

    **x** — physical model x coordinate.
    """

    return int(x*scale_factor) + window_width//2


def scale_y(y):
    """Calculates screen **x** coordinate using model **x** coordinate.
    Takes float, returns integer.
    if the resulting **x** exceeds screen dimensions - the exceeding coordinate is returned.
    **y** axis direction is reversed, cause in physical model it is upwards, whereas on canvas it's downwards.
    
    Parametres:

    **y** — model y coordinate.
    """

    return y  # FIXME: not done yet


def create_star_image(space, star):
    """
    Parametres:

    **space** — canvas.
    **star** — star object.
    """

    x = scale_x(star.x)
    y = scale_y(star.y)
    r = star.R
    star.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=star.color)


def create_planet_image(space, planet):
    """
    Parametres:

    **space** — canvas.
    **planet** — planet object.
    """
    pass  # FIXME: implement like create_star_image(space, star)


def update_system_name(space, system_name):
    """Writes text on canvas with object names

    Params:

    **space** — canvas.
    **system_name** — object system name.
    """
    space.create_text(30, 80, tag="header", text=system_name, font=header_font)


def update_object_position(space, body):
    """Moves objects on cnvas.

    Params:

    **space** — canvas.
    **body** — the object to be moved.
    """
    x = scale_x(body.x)
    y = scale_y(body.y)
    r = body.R
    if x + r < 0 or x - r > window_width or y + r < 0 or y - r > window_height:
        space.coords(body.image, window_width + r, window_height + r,
                     window_width + 2*r, window_height + 2*r)  # положить за пределы окна
    space.coords(body.image, x - r, y - r, x + r, y + r)


if __name__ == "__main__":
    print("This module is not for direct call!")
