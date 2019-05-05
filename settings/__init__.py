# Google Fonts Sync
# by Kilian Friedrich
#
# 2019-05-04
#
# settings/__init__.py:
#
# This script includes functions for settings  (get and set)

from os.path import dirname
from pickle import dump, load

# the path to this folder (needed bc the setting file is located here)
SCRIPT_DIR = dirname(__file__) + '/'

SETTINGS_FILE_NAME = 'settings'  # change this if filename changes
SETTINGS_FILE_PATH = SCRIPT_DIR + SETTINGS_FILE_NAME
SETTINGS = load(open(SETTINGS_FILE_PATH, 'rb'))  # open dict in file via pickle.load()


# writes a value to a key and stores all settings
# creates a new setting if key was not found
def set_setting(key, value):

    SETTINGS[key] = value
    __write_settings__()  # write all settings to file


# returns a string
def get_setting(key):

    return SETTINGS.get(key)


# shouldn't be called from outside
# uses pickle to store the settings dict
def __write_settings__():

    dump(SETTINGS, open(SETTINGS_FILE_PATH, 'wb'))
