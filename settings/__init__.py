from os.path import dirname
from pickle import dump, load

SCRIPT_DIR = dirname(__file__) + '/'

USER_SETTINGS_FILE_NAME = 'user_settings'
USER_SETTINGS_FILE_PATH = SCRIPT_DIR + USER_SETTINGS_FILE_NAME
USER_SETTINGS = load(open(USER_SETTINGS_FILE_PATH, 'rb'))
USER_SETTINGS_KEYS = USER_SETTINGS.keys()


def set_setting(key, value):

    if key not in USER_SETTINGS_KEYS:

        return

    USER_SETTINGS[key] = value
    __write_settings__()


def get_setting(key):

    return USER_SETTINGS.get(key)


def __write_settings__():

    dump(USER_SETTINGS, open(USER_SETTINGS_FILE_PATH, 'wb'))
