from gfonts_values import MIN_STYLECOUNT, MAX_STYLECOUNT
from filter import IGNORED_KEYWORD


def get_stylecount(stylecount):

    return Stylecount(stylecount) if MIN_STYLECOUNT <= int(stylecount) <= MAX_STYLECOUNT else IGNORED_KEYWORD


class Stylecount:

    def __init__(self, stylecount):

        self.stylecount = int(stylecount)

    def __eq__(self, other):

        return self.stylecount == other.stylecount if isinstance(other, Stylecount) else False

    def __le__(self, other):

        return self.stylecount <= other
