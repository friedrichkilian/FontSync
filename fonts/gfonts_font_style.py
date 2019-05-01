# Google Fonts Sync
# by Kilian Friedrich
#
# 2019-04-28
#
# fonts/gfonts_font_style.py:
#
# This script holds the FontStyle class (which represents a font style)

from gfonts_values import get_thickness, get_slant, get_width


# this class represents a font style and stores its values
class FontStyle:

    # constructor, takes style name and style details
    def __init__(self, name, details):

        self.id = name

        # always store None if there are no details given
        self.thickness = get_thickness(details['thickness']) if details is not None else None
        self.slant = get_slant(details['slant']) if details is not None else None
        self.width = get_width(details['width']) if details is not None else None

    # returns False if a font style couldn't store any details
    def has_details(self):

        return self.thickness is not None and self.slant is not None and self.width is not None
