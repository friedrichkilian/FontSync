from settings import get_setting
from filter import IGNORED_KEYWORD

CATEGORIES = get_setting('gfonts_categories')

SUBSETS = get_setting('gfonts_subsets')

MIN_STYLECOUNT = get_setting('gfonts_stylecount_min')
MAX_STYLECOUNT = get_setting('gfonts_stylecount_max')

MIN_THICKNESS = get_setting('gfonts_thickness_min')
MAX_THICKNESS = get_setting('gfonts_thickness_max')

MIN_SLANT = get_setting('gfonts_slant_min')
MAX_SLANT = get_setting('gfonts_slant_max')

MIN_WIDTH = get_setting('gfonts_width_min')
MAX_WIDTH = get_setting('gfonts_width_max')


def get_category_list(categories):

    category_list = [category for category in categories if category in CATEGORIES]
    return category_list if len(category_list) > 0 and IGNORED_KEYWORD not in category_list else IGNORED_KEYWORD


def get_slant(slant):

    return slant if MIN_SLANT <= slant <= MAX_SLANT else IGNORED_KEYWORD


def get_stylecount(stylecount):

    return stylecount if MIN_STYLECOUNT <= stylecount <= MAX_STYLECOUNT else IGNORED_KEYWORD


def get_subset(subset):

    return subset if subset in SUBSETS else IGNORED_KEYWORD


def get_subsets(subsets):

    subset_list = [subset for subset in subsets if subset in SUBSETS]
    return subset_list if len(subset_list) > 0 else IGNORED_KEYWORD


def get_thickness(thickness):

    return thickness if MIN_THICKNESS <= thickness <= MAX_THICKNESS else IGNORED_KEYWORD


def get_width(width):

    return width if MIN_WIDTH <= width <= MAX_WIDTH else IGNORED_KEYWORD
