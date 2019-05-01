from logging import log
from filter import IGNORED  # if a filter value is equal to this variable, it will be ignored


def filter_fonts(fonts, category_list, subset, stylecount, slant, thickness, width):

    return [font for font in fonts
            if __filter_font_family__(font, category_list, subset, stylecount, slant, thickness, width)]


def __filter_font_family__(font_family, category_list, subset, stylecount, slant, thickness, width):

    log('Checking ' + font_family.family_name + '...')

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
