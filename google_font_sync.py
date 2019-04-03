import ssl as https_config
from sys import argv as arguments
from urllib import request as internet
from glob import glob as get_files
from zipfile import ZipFile as ZIPFile
from json import loads as parse
from os import makedirs as make_dir, remove as remove_file

from settings.settings_dict import get_setting

# gets Google's JSON file which stores all fonts
# & transfers them into a new list of fonts which is smaller in size
def get_available_fonts():

    json_string = internet.urlopen(get_setting('gfonts_url_json')).read().decode('utf-8')
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
        if category_lower in get_setting('gfonts_categories').keys():

            category_list.append(get_setting('gfont_categories')[category_lower])

    if len(category_list) == 0:

        return get_setting('keyword_all')

    return category_list


# returns the number of the IGNORED_KEYWORD when the number is outside the range
def keep_in_range(string, min_value, max_value):

    num = int(string)

    if num < min_value:

        return get_setting('keyword_all')

    if num > max_value:

        return get_setting('keyword_all')

    return num


# syncs with Google Fonts
def sync(category_arg, subset_arg, stylecount_arg, thickness_arg, slant_arg, width_arg):

    category_list = get_category_list(category_arg)
    corrected_subset = get_setting('gfonts_subsets').get(subset_arg.lower(), 'all')

    corrected_stylecount = keep_in_range(stylecount_arg, get_setting('gfonts_stylecount_min'),
                                         get_setting('gfonts_stylecount_max'))
    corrected_thickness = keep_in_range(thickness_arg, get_setting('gfonts_thickness_min'),
                                        get_setting('gfonts_thickness_max'))
    corrected_slant = keep_in_range(slant_arg, get_setting('gfonts_slant_min'), get_setting('gfonts_slant_max'))
    corrected_width = keep_in_range(width_arg, get_setting('gfonts_width_min'), get_setting('gfonts_width_max'))

    available_fonts = get_available_fonts()

    filtered_fonts = []
    for font in available_fonts:

        if category_list != get_setting('keyword_all') and font['category'] not in category_list:

            continue

        if corrected_subset != get_setting('keyword_all') and corrected_subset not in font['subsets']:

            continue

        if corrected_stylecount != get_setting('keyword_all') and font['stylecount'] < corrected_stylecount:

            continue

        if corrected_thickness != get_setting('keyword_all') and corrected_thickness not in font['thickness']:

            continue

        if corrected_slant != get_setting('keyword_all') and corrected_slant not in font['slant']:

            continue

        if corrected_width != get_setting('keyword_all') and corrected_width not in font['width']:

            continue

        filtered_fonts.append(font['family'])

    for font in filtered_fonts:

        dir_name = font.replace(' ', get_setting('output_dir_space_replacement'))
        dir_path = get_setting('output_dir').format(dir_name)
        zip_path = dir_path + '.zip'

        download_name = font.replace(' ', get_setting('gfonts_url_download_space_replacement'))
        download_url = get_setting('gfonts_url_download').format(download_name)

        internet.urlretrieve(download_url, zip_path)
        zip_file = ZIPFile(zip_path, 'r')

        make_dir(dir_path, exist_ok=True)
        files = get_files(zip_path + '/*')
        for f in files:
            remove_file(f)

        zip_file.extractall(dir_path)
        remove_file(zip_path)


# syncs with 'all' for everything
def default_sync():

    sync('all', 'all', 'all', 'all', 'all', 'all')


# noinspection PyProtectedMember
https_config._create_default_https_context = https_config._create_unverified_context
make_dir('/Library/Fonts/GoogleFonts', exist_ok=True)

if len(arguments) == 7:
    sync(arguments[1], arguments[2], arguments[3], arguments[4], arguments[5], arguments[6])

else:
    default_sync()
