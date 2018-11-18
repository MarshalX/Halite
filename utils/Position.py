from hlt.positionals import Position


def normalize(position, width=32, height=32):
    """
    Normalized the position within the bounds of the toroidal map.
    i.e.: Takes a point which may or may not be within width and
    height bounds, and places it within those bounds considering
    wraparound.
    :param height:
    :param width:
    :param position: A position object.
    :return: A normalized position object fitting within the bounds of the map
    """
    return Position(position.x % width, position.y % height)
