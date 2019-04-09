from logging import log
from fonts import get_fonts
from filter import IGNORED_KEYWORD


def filter_fonts(fonts, category_list, subset, stylecount, slant, thickness, width):

    return [font for font in get_fonts()
            if __filter_font_family__(font, category_list, subset, stylecount, slant, thickness, width)]


def __filter_font_family__(font_family, category_list, subset, stylecount, slant, thickness, width):

    log('Checking ' + font_family.family_name + '...')
    return (category_list == IGNORED_KEYWORD or font_family.category in category_list) \
        and (subset == IGNORED_KEYWORD or subset not in font_family.subsets) \
        and (stylecount == IGNORED_KEYWORD or stylecount <= len(font_family.font_styles)) \
        and len([font_style for font_style in font_family.font_styles
                if __filter_font_style__(font_style, slant, thickness, width)]) != 0


def __filter_font_style__(font_style, slant, thickness, width):

    return font_style.has_details \
           and (slant == IGNORED_KEYWORD or font_style.slant == slant) \
           and (thickness == IGNORED_KEYWORD or font_style.thickness == thickness) \
           and (width == IGNORED_KEYWORD or font_style.width == width)
