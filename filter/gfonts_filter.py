# Google Fonts Sync
# by Kilian Friedrich
#
# 2019-04-28
#
# filter/gfonts_filter.py:
#
# This script filters a list of Google Fonts when the filter_fonts() function is called.
# All other functions are needed for filter_fonts() and aren't meant to be called from outside!
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

from logging import log
from filter import IGNORED  # if a filter value is equal to this variable, it will be ignored
from fonts import get_all_gfonts


# returns a list of fonts which fulfill the filter
# takes filter specifications as parameters
def filter_fonts(category_list, subset, stylecount, slant, thickness, width, gui=None):

    if gui is None:

        return [font for font in get_all_gfonts()
                if __filter_font_family__(font, category_list, subset, stylecount, slant, thickness, width)]

    all_fonts = get_all_gfonts()
    filtered_fonts = list()

    gui[2].config(max=len(all_fonts))

    for i in range(0, len(all_fonts)):

        gui[0].set(i)
        if __filter_font_family__(all_fonts[i], category_list, subset, stylecount, slant, thickness, width, gui[1]):

            filtered_fonts.append(all_fonts[i])

    gui[0].set(0)

    return filtered_fonts


# returns True if a font fulfills the filter
# takes filter specification as parameters
def __filter_font_family__(font_family, category_list, subset, stylecount, slant, thickness, width, label=None):

    log('Checking ' + font_family.family_name + '...', lbl=label)  # log 'Checking [...]...'

    return (category_list is IGNORED or font_family.category.lower().replace(' ', '-') in category_list) \
        and (subset is IGNORED or subset in font_family.subsets) \
        and (stylecount is IGNORED or stylecount <= len(font_family.font_styles)) \
        and len([font_style for font_style in font_family.font_styles
                if __filter_font_style__(font_style, slant, thickness, width)]) > 0


# returns True if a font style fulfills the filter
# takes filter specification as parameters
def __filter_font_style__(font_style, slant, thickness, width):

    return font_style.has_details \
           and (slant is IGNORED or font_style.slant == slant) \
           and (thickness is IGNORED or font_style.thickness == thickness) \
           and (width is IGNORED or font_style.width == width)
