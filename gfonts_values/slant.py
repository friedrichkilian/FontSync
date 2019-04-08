from gfonts_values import MIN_SLANT, MAX_SLANT
from filter import IGNORED_KEYWORD


def get_slant(slant):

    return Slant(slant) if MIN_SLANT <= int(slant) <= MAX_SLANT else IGNORED_KEYWORD


class Slant:

    def __init__(self, slant):

        self.slant = int(slant)

    def __eq__(self, other):

        return self.slant == other.slant if isinstance(other, Slant) else False
