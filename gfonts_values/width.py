from gfonts_values import MIN_WIDTH, MAX_WIDTH
from filter import IGNORED_KEYWORD


def get_width(width):
    return Width(width) if MIN_WIDTH <= int(width) <= MAX_WIDTH else IGNORED_KEYWORD


class Width:

    def __init__(self, width):
        self.width = int(width)

    def __eq__(self, other):

        return self.width == other.width if isinstance(other, Width) else False
