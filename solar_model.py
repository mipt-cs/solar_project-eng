# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Newton's constant G"""


def calculate_force(body, space_objects):
    """Computes the forcce acting on a body.

    Parametres:

    **body** — the one on which the force acts.
    **space_objects** — list of acting objects (force-making).
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # body's gravitational force doesn't act on itself!
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        body.Fx += 1  # FIXME: insert formula...
        body.Fy += 2  # FIXME: insert formula...


def move_space_object(body, dt):
    """Moves the body according to the force.

    Parametres:

    **body** — the body to be moved.
    """

    ax = body.Fx/body.m
    body.x += 42  # FIXME: how to move...
    body.Vx += ax*dt
    # FIXME: not done recalculation of y coordinate!


def recalculate_space_objects_positions(space_objects, dt):
    """recomputes object positions.

    Parametres:

    **space_objects** — list of objects to move.
    **dt** — timestep
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
