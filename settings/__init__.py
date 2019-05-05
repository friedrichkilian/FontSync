# Google Fonts Sync
# by Kilian Friedrich
#
# 2019-05-04
#
# settings/__init__.py:
#
# This script holds all user settings. When first loaded, the script will fetch all user settings from the 'settings'
# file of this folder. The settings are stored inside a dictionary, every setting consists of a key and a value (e.g.
# the output directory: key='output_dir', value='...'). Settings are always stored and returned as strings!
# There are two kinds of accesses which possible after the script initialized:
#   1. Get a specific setting (using get_setting(key)) - Returns the value which belongs to the given key or an empty
#                                                        string if the key wasn't found.
#   2. Set a specific setting (using set_setting(key)) - Sets the value which belongs to the key to the given value.
#                                                        A new setting will be created if the key wasn't found so be
#                                                        careful with this function!
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

from os.path import dirname
from pickle import dump, load

# the path to this folder (needed bc the setting file is located here)
SCRIPT_DIR = dirname(__file__) + '/'

SETTINGS_FILE_NAME = 'settings'  # change this if filename changes
SETTINGS_FILE_PATH = SCRIPT_DIR + SETTINGS_FILE_NAME
SETTINGS = load(open(SETTINGS_FILE_PATH, 'rb'))  # open dict in file via pickle.load()


# writes a value to a key and stores all settings
# creates a new setting if key was not found
def set_setting(key, value=None):

    SETTINGS[key] = value
    __write_settings__()  # write all settings to file


# returns a string
def get_setting(key):

    return SETTINGS.get(key, '')


# shouldn't be called from outside
# uses pickle to store the settings dict
def __write_settings__():

    dump(SETTINGS, open(SETTINGS_FILE_PATH, 'wb'))
