from os.path import dirname
from pickle import dump, load

SCRIPT_DIR = dirname(__file__) + '/'

USER_SETTINGS_FILE_NAME = 'user_settings'
USER_SETTINGS_FILE_PATH = SCRIPT_DIR + USER_SETTINGS_FILE_NAME
USER_SETTINGS = load(open(USER_SETTINGS_FILE_PATH, 'rb'))
USER_SETTINGS_KEYS = USER_SETTINGS.keys()

CONST_SETTINGS_FILE_NAME = 'const_settings'
CONST_SETTINGS_FILE_PATH = SCRIPT_DIR + CONST_SETTINGS_FILE_NAME
CONST_SETTINGS = load(open(CONST_SETTINGS_FILE_PATH, 'rb'))


def set_setting(key, value):

    if key not in USER_SETTINGS_KEYS:
        return

    USER_SETTINGS[key] = value
    __write_settings__()


def get_setting(key):

    return CONST_SETTINGS.get(key, USER_SETTINGS.get(key))


def __write_settings__():

    dump(USER_SETTINGS, open(USER_SETTINGS_FILE_PATH, 'wb'))

str = {'gfonts_categories': {'serif': 'Serif', 'sans-serif': 'Sans Serif', 'display': 'Display', 'handwriting': 'Handwriting', 'monospace': 'Monospace'}, 'gfonts_subsets': {'arabic': 'Arabic', 'bengali': 'Bengali', 'chinese-simplified': 'Chinese (Simplified)', 'chinese-traditional': 'Chinese (Traditional)', 'cyrillic': 'Cyrillic', 'cyrillic-ext': 'Cyrillic (Extended)', 'devanagari': 'Devanagari', 'greek': 'Greek', 'greek-ext': 'Greek (Extended)', 'gujarati': 'Gujarati', 'gurmukhi': 'Gurmukhi', 'hebrew': 'Hebrew', 'japanese': 'Japanese', 'kannada': 'Kannada', 'khmer': 'Khmer', 'korean': 'Korean', 'latin': 'Latin', 'latin-ext': 'Latin (Extended)', 'malayalam': 'Malayalam', 'myanmar': 'Myanmar', 'oriya': 'Oriya', 'sinhala': 'Sinhala', 'tamil': 'Tamil', 'telugu': 'Telugu', 'thai': 'Thai', 'vietnamese': 'Vietnamese'}, 'gfonts_url_json': 'https://fonts.google.com/metadata/fonts', 'gfonts_url_download': 'https://fonts.google.com/download?family={}', 'gfonts_url_download_space_replacement': '+', 'gfonts_stylecount_min': 2, 'gfonts_stylecount_max': 19, 'gfonts_thickness_min': 1, 'gfonts_thickness_max': 10, 'gfonts_slant_min': 1, 'gfonts_slant_max': 10, 'gfonts_width_min': 1, 'gfonts_width_max': 10, 'keyword_all': 'all', 'separator': ','}
dump(str, open(CONST_SETTINGS_FILE_PATH, 'wb'))