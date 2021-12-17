# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Reads object data from file, creates objects, calls corresponding drawing functions.
    
    Parametres:

    **input_filename** — filename of the file with object spesifications
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # empty strings and comments are left away
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXME: do the same for planet
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Reads data from a single string. 
    The string should have the specified format:
    Star <radius in pixels> <colour> <mass> <x> <y> <Vx> <Vy>

    (x, y) — star coordinates, (Vx, Vy) — its velocity.
    Example:
    Star 10 red 1000 1 2 3 4

    Parametres:

    **line** — string with object data.
    **star** — object to specify.
    """

    pass  # FIXME: not done yet

def parse_planet_parameters(line, planet):
    """Reads planet data from a string of the fixed format:
    Planet <radius in pixels> <colour> <mass> <x> <y> <Vx> <Vy>

    (x, y) — planet coordinates, (Vx, Vy) — planet velocity.
    String example:
    Planet 10 red 1000 1 2 3 4

    Parametres:

    **line** — strig with planet data.
    **planet** — planet object to specify.
    """
    pass  # FIXME: not done yet...


def write_space_objects_data_to_file(output_filename, space_objects):
    """Saves object data to file. File strngs will be of the following format:
    Star <radius in pixels> <colour> <mass> <x> <y> <Vx> <Vy>
    Planet <radius in pixels> <colour> <mass> <x> <y> <Vx> <Vy>

    Parametres:

    **output_filename** — filename of the file to be saved
    **space_objects** — list of objects to be written down
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            # FIXME: should store real values

# FIXME: better also to implify a function, saving dynamics history to file...

if __name__ == "__main__":
    print("This module is not for direct call!")
