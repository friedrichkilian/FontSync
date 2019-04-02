import ssl as https_config
from sys import argv as arguments
from urllib import request as internet
from glob import glob as get_files
from zipfile import ZipFile as ZIPFile
from json import loads as parse
from os import makedirs as make_dir, remove as remove_file

# accepted values for "category"
# & their equivalent which are used in Google's JSON file (which are readable so they're used while logging too)
# values are ignored if they're not one of these
CATEGORIES = {
    'serif': 'Serif',
    'sans-serif': 'Sans Serif',
    'display': 'Display',
    'handwriting': 'Handwriting',
    'monospace': 'Monospace'
}

# accepted values for "subset"
# & their readable equivalent which are used while logging
# values are ignored if they're not one of these
SUBSETS = {
    'arabic': 'Arabic',
    'bengali': 'Bengali',
    'chinese-simplified': 'Chinese (Simplified)',
    'chinese-traditional': 'Chinese (Traditional)',
    'cyrillic': 'Cyrillic',
    'cyrillic-ext': 'Cyrillic (Extended)',
    'devanagari': 'Devanagari',
    'greek': 'Greek',
    'greek-ext': 'Greek (Extended)',
    'gujarati': 'Gujarati',
    'gurmukhi': 'Gurmukhi',
    'hebrew': 'Hebrew',
    'japanese': 'Japanese',
    'kannada': 'Kannada',
    'khmer': 'Khmer',
    'korean': 'Korean',
    'latin': 'Latin',
    'latin-ext': 'Latin (Extended)',
    'malayalam': 'Malayalam',
    'myanmar': 'Myanmar',
    'oriya': 'Oriya',
    'sinhala': 'Sinhala',
    'tamil': 'Tamil',
    'telugu': 'Telugu',
    'thai': 'Thai',
    'vietnamese': 'Vietnamese'
}

GOOGLE_FONTS_JSON_URL = 'https://fonts.google.com/metadata/fonts'
GOOGLE_FONTS_DOWNLOAD_URL = 'https://fonts.google.com/download?family={}'
GOOGLE_FONTS_DOWNLOAD_URL_SPACE_REPLACEMENT = '+'

FONTS_DIR = '/Library/Fonts/GoogleFonts/{}'
FONTS_DIR_SPACE_REPLACEMENT = ''

MIN_STYLECOUNT = 1
MAX_STYLECOUNT = 19
MIN_THICKNESS = 0
MAX_THICKNESS = 10
MIN_SLANT = 0
MAX_SLANT = 10
MIN_WIDTH = 0
MAX_WIDTH = 10

IGNORED_KEYWORD = 'all'
SEPARATOR = ','


# gets Google's JSON file which stores all fonts
# & transfers them into a new list of fonts which is smaller in size
def get_available_fonts():

    json_string = internet.urlopen(GOOGLE_FONTS_JSON_URL).read().decode('utf-8')
    json_string = str(json_string).replace('\\n', '\n').lstrip(')]}\'\n')
    family_metadata_list = parse(json_string)['familyMetadataList']
    available_fonts = []

    for family_metadata in family_metadata_list:

        font = {
            'family': family_metadata['family'],
            'category': family_metadata['category'],
            'subsets': [],
            'stylecount': len(family_metadata['fonts']),
            'thickness': [],
            'slant': [],
            'width': []
        }

        for family_metadata_subset in family_metadata['subsets']:

            if not family_metadata_subset == 'menu':

                font['subsets'].append(family_metadata_subset)

        for k, subfont_google in family_metadata['fonts'].items():

            if subfont_google is None:

                continue

            thickness = subfont_google['thickness']
            slant = subfont_google['slant']
            width = subfont_google['width']

            if thickness not in font['thickness']:

                font['thickness'].append(int(thickness))

            if slant not in font['slant']:

                font['slant'].append(int(slant))

            if width not in font['width']:

                font['width'].append(int(width))

        available_fonts.append(font)

    return available_fonts


# returns a list of strings of CATEGORIES or the IGNORED_KEYWORD
def get_category_list(categories_string):

    category_list = []
    for category in categories_string:

        category_lower = category.lower()
        if category_lower in CATEGORIES.keys():

            category_list.append(CATEGORIES[category_lower])

    if len(category_list) == 0:

        return IGNORED_KEYWORD

    return category_list


# keeps the given number (as string) inside the given range
def keep_in_range(string, min_value, max_value):

    num = int(string)

    if num < min_value:

        return IGNORED_KEYWORD

    if num > max_value:

        return IGNORED_KEYWORD

    return num


# syncs with Google Fonts
def sync(category_arg, subset_arg, stylecount_arg, thickness_arg, slant_arg, width_arg):

    category_list = get_category_list(category_arg)
    corrected_subset = SUBSETS.get(subset_arg.lower(), 'all')

    corrected_stylecount = keep_in_range(stylecount_arg, MIN_STYLECOUNT, MAX_STYLECOUNT)
    corrected_thickness = keep_in_range(thickness_arg, MIN_THICKNESS, MAX_THICKNESS)
    corrected_slant = keep_in_range(slant_arg, MIN_SLANT, MAX_SLANT)
    corrected_width = keep_in_range(width_arg, MIN_WIDTH, MAX_WIDTH)

    available_fonts = get_available_fonts()

    filtered_fonts = []
    for font in available_fonts:

        if category_list != IGNORED_KEYWORD and font['category'] not in category_list:

            continue

        if corrected_subset != IGNORED_KEYWORD and corrected_subset not in font['subsets']:

            continue

        if corrected_stylecount != IGNORED_KEYWORD and font['stylecount'] < corrected_stylecount:

            continue

        if corrected_thickness != IGNORED_KEYWORD and corrected_thickness not in font['thickness']:

            continue

        if corrected_slant != IGNORED_KEYWORD and corrected_slant not in font['slant']:

            continue

        if corrected_width != IGNORED_KEYWORD and corrected_width not in font['width']:

            continue

        filtered_fonts.append(font['family'])

    for font in filtered_fonts:

        dir_name = font.replace(' ', FONTS_DIR_SPACE_REPLACEMENT)
        dir_path = FONTS_DIR.format(dir_name)
        zip_path = dir_path + '.zip'

        download_name = font.replace(' ', GOOGLE_FONTS_DOWNLOAD_URL_SPACE_REPLACEMENT)
        download_url = GOOGLE_FONTS_DOWNLOAD_URL.format(download_name)

        internet.urlretrieve(download_url, zip_path)
        zip_file = ZIPFile(zip_path, 'r')

        make_dir(dir_path, exist_ok=True)
        files = get_files(zip_path + '/*')
        for f in files:
            remove_file(f)

        zip_file.extractall(dir_path)
        remove_file(zip_path)


# syncs with 'all', 'all
def default_sync():

    sync('all', 'all', 'all', 'all', 'all', 'all')


# noinspection PyProtectedMember
https_config._create_default_https_context = https_config._create_unverified_context
make_dir('/Library/Fonts/GoogleFonts', exist_ok=True)

if len(arguments) == 7:
    sync(arguments[1], arguments[2], arguments[3], arguments[4], arguments[5], arguments[6])

else:
    default_sync()
