# Google Fonts Sync
# by Kilian Friedrich
#
# 2019-04-28
#
# gfonts_values/__init__.py:
#
# This script has two functions:
#   1. It stores acceptable values for every filter option.
#   2. It returns guilty filter values when wrong ones are given (via get_*() functions).
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

from filter import IGNORED

# available categories
CATEGORIES = ['serif', 'sans-serif', 'display', 'handwriting', 'monospace']

# available subsets
SUBSETS = ['arabic', 'bengali', 'chinese-simplified', 'chinese-traditional', 'cyrillic', 'cyrillic-ext', 'devanagari',
           'greek', 'greek-ext', 'gujarati', 'gurmukhi', 'hebrew', 'japanese', 'kannada', 'khmer', 'korean', 'latin',
           'latin-ext', 'malayalam', 'myanmar', 'oriya', 'sinhala', 'tamil', 'telugu', 'thai', 'vietnamese']

# borders of stylecount (2 to 18)
# 1 is possible but means the same as IGNORED since every font has 1+ font styles
MIN_STYLECOUNT = 2
MAX_STYLECOUNT = 18

# borders of thickness (1 to 10)
MIN_THICKNESS = 1
MAX_THICKNESS = 10

# borders of slant (1 to 10)
MIN_SLANT = 1
MAX_SLANT = 10

# borders of width (1 to 10)
MIN_WIDTH = 1
MAX_WIDTH = 10


# returns a good list of categories
def get_category_list(categories):

    # all categories from the given list which are ok
    category_list = [category for category in categories if category in CATEGORIES]

    # return IGNORED if list is empty (= no category in given list is ok)
    return category_list if len(category_list) > 0 else IGNORED


# returns a slant (if the given slant is inside slant's borders) or IGNORED (if it's not)
def get_slant(slant):

    return slant if MIN_SLANT <= slant <= MAX_SLANT else IGNORED


# returns a stylecount (if the given stylecount is inside stylecount's borders) or IGNORED (if it's not)
def get_stylecount(stylecount):

    return stylecount if MIN_STYLECOUNT <= stylecount <= MAX_STYLECOUNT else IGNORED


# returns a subset (if the given subset is ok) or IGNORED (if it's not)
def get_subset(subset):

    return subset if subset in SUBSETS else IGNORED


# returns a good list of categories
def get_subsets(subsets):

    # all subsets from the given list which are ok
    subset_list = [subset for subset in subsets if subset in SUBSETS]

    # return IGNORED if list is empty (= no subset in given list is ok)
    return subset_list if len(subset_list) > 0 else IGNORED


# returns a thickness (if the given thickness is inside thickness's borders) or IGNORED (if it's not)
def get_thickness(thickness):

    return thickness if MIN_THICKNESS <= thickness <= MAX_THICKNESS else IGNORED


# returns a width (if the given width is inside width's borders) or IGNORED (if it's not)
def get_width(width):

    return width if MIN_WIDTH <= width <= MAX_WIDTH else IGNORED
