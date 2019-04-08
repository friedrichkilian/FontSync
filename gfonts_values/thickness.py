from gfonts_values import MIN_THICKNESS, MAX_THICKNESS
from filter import IGNORED_KEYWORD


def get_thickness(thickness):

    return Thickness(thickness) if MIN_THICKNESS <= int(thickness) <= MAX_THICKNESS else IGNORED_KEYWORD


class Thickness:

    def __init__(self, thickness):

        self.thickness = int(thickness)

    def __eq__(self, other):

        return self.thickness == other.thickness if isinstance(other, Thickness) else False
