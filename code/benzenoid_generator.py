#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt  # Used only for drawing

"""
Suppose that the infinite hexagonal lattice is equipped with
a coordinate system. Any benzenoid system can be represented
as a list of hexagons, e.g. [(1, 2), (1, 3), (2, 2)]. 
"""

def to_canonical_trans(b):
    """
    Transform the benzenoid system so that all coordinates are
    non-negative integers and as small as possible.

    Example: [(1, 2), (1, 3), (2, 2)] -> [(0, 0), (0, 1), (1, 0)]
    """
    i_min = min(i for (i, j) in b)
    j_min = min(j for (i, j) in b)
    return sorted([(i - i_min, j - j_min) for (i, j) in b])

def rotation_60(b):
    """
    Rotate the benzenoid system by 60 degrees in the counter-clockwise
    direction.
    """
    return [(i + j, -i) for (i, j) in b]

def reflection(b):
    """
    Reflect the benzenoid system over a line.
    """
    return [(-i, i + j) for (i, j) in b]

def to_canonical(b):
    """
    Return the canonical form of a benzenoid system b. All symmetries
    of benzenoid systems are taken into account.
    """
    l = [to_canonical_trans(b)]
    r = [to_canonical_trans(reflection(b))]
    for i in range(5):
        l.append(to_canonical_trans(rotation_60(l[-1])))
        r.append(to_canonical_trans(rotation_60(r[-1])))
    return tuple(min(min(l), min(r)))

def are_isomorphic(b1, b2):
    """
    Return True if benzenoid system b1 and b2 are isomorphic.
    """
    return to_canonical(b1) == to_canonical(b2)

def neighbours(h):
    """
    Return the list of neighbours of a hexagon h = (i, j).
    """
    i, j = h
    return [(i + 1, j), (i + 1, j - 1), (i, j - 1),
            (i - 1, j), (i - 1, j + 1), (i, j + 1)]

def layer_of_fat(b):
    """
    Return the list of all hexagons that are adjacent to some
    hexagon of b, but do not belong to b.
    """
    f = set()
    for h in b:
        for n in neighbours(h):
            if n not in b:
                f.add(n)
    return list(f)

def list_of_benzenoids(h):
    """
    Return the list of all benzenoid system with h hexagons.
    All benzenoids are in the canonical form.
    """
    l = [((0, 0),)]  # Benzene

    for i in range(h - 1):
        l_new = set()
        for b in l:
            f = layer_of_fat(b)
            for hex in f:
                l_new.add(to_canonical(b + (hex,)))
        l = list(l_new)

    return l

def get_vertices(h):
    """
    Return the coordinates of vertices of a hexagon.
    """
    i, j = h
    vertices = [(math.sqrt(3) / 2, 1 / 2), (0, 1), (-math.sqrt(3) / 2, 1 / 2),
               (-math.sqrt(3) / 2, -1 / 2), (0, -1), (math.sqrt(3) / 2, -1 / 2)]
    x_centre, y_centre = math.sqrt(3) * j + math.sqrt(3) / 2 * i, 3 / 2 * i
    return [x_centre + x for x, _ in vertices], [y_centre + y for _, y in vertices]

def draw_benzenoid(b, file_name):
    """
    Draw the benzenoid system b and save the image to the file
    named file_name.
    """
    fig = plt.figure()
    plt.axis('equal')
    for h in b:
        x_list, y_list = get_vertices(h)
        plt.fill(x_list, y_list, facecolor='lightsalmon', edgecolor='orangered', linewidth=2)
    fig.savefig(file_name)
    plt.close(fig)

if __name__ == '__main__':
    h = 5
    l = list_of_benzenoids(h)
    print('Number of benzenoid systems on {0} hexagons: {1}'.format(h, len(l)))
    print('The list of all benzenoid systems:')
    for i, b in enumerate(l):
        print("{0:4d}  {1}".format(i + 1, b))
        draw_benzenoid(b, 'img/benzenoid_{0}_{1:02d}.png'.format(h, i + 1))
