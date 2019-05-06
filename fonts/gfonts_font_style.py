# Google Fonts Sync
# by Kilian Friedrich
#
# 2019-04-28
#
# fonts/gfonts_font_style.py:
#
# This script holds the FontStyle class which represents a font style. Named class just stores information about a font
# style so it's more like a struct from C than a class.
#
# Copyright after CC BY-NC-SA 4.0
# You are free to:
#   SHARE - copy and redistribute the material in any medium or format
#   ADAPT - remix, transform, and build upon the material
# Under the following terms:
#   ATTRIBUTION - You must give appropriate credit, provide a link to the license, and indicate if changes were made.
#                 You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or
#                 your use.
#   NONCOMMERCIAL - You may not use the material for commercial purposes.
#   SHAREALIKE - If you remix, transform, or build upon the material, you must distribute your contributions under the
#                same license as the original.
# Follow https://creativecommons.org/licenses/by-nc-sa/4.0/ for more information.

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
