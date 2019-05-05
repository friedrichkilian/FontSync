# Google Fonts Sync
# by Kilian Friedrich
#
# 2019-04-28
#
# fonts/gfonts_font_family.py:
#
# This script holds the FontFamily class which represents a font. Named class just stores information about a font
# family so it's more like a struct from C than a class.
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

from datetime import date  # this is a class (don't ask why it doesn't start with a capital)

from fonts.gfonts_font_style import FontStyle
from gfonts_values import get_subsets


# this class represents a font and stores its values and a list of its styles
class FontFamily:

    # constructor, takes a dict of values (extracted directly from Google's JSON)
    def __init__(self, details):

        self.family_name = details['family']
        self.category = details['category']
        self.size = details['size']
        self.designers = details['designers']
        self.subsets = get_subsets(details['subsets'])

        # the date is given as string like 'DD-MM-YYYY'
        # since the constructor of a date needs DD, MM and YYYY separately, the string must be split
        date_added = details['dateAdded'].split('-')
        self.date_added = date(int(date_added[0]), int(date_added[1]), int(date_added[2]))

        # the date is given as string like 'DD-MM-YYYY'
        # since the constructor of a date needs DD, MM and YYYY separately, the string must be split
        last_modified = details['lastModified'].split('-')
        self.last_modified = date(int(last_modified[0]), int(last_modified[1]), int(last_modified[2]))

        # collect font styles and store them
        self.font_styles = [FontStyle(font_style_id, font_style_details) for font_style_id, font_style_details
                            in details['fonts'].items()]
