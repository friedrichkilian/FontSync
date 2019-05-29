# Google Fonts Sync
# by Kilian Friedrich
#
# 2019-04-28
#
# fonts/__init__.py:
#
# This script downloads information about all fonts from Google Fonts and returns them, all in the function
# get_all_gfonts(). It uses a JSON file from Google which is located at https://fonts.google.com/metadata/fonts.
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

from json import loads as parse  # is used to parse Google's JSON file about their fonts
from urllib.request import urlopen as fetch_internet_file  # is used to download Google's JSON file about their fonts
import ssl as https_config

from fonts.gfonts_font_family import FontFamily

JSON_DOWNLOAD_URL = 'https://fonts.google.com/metadata/fonts'  # the JSON file is stored here

# SSL doesn't work (idk why) so just disable it?
# maybe not the best workaround but better than nothing
# noinspection PyProtectedMember
https_config._create_default_https_context = https_config._create_unverified_context

json_download = fetch_internet_file(JSON_DOWNLOAD_URL)  # fetch Google's JSON

# Google's JSON is weirdly encoded, has escaped line breaks and begins with ')]}'' for some reason
# this line will convert the JSON to a readable file
json_string = json_download.read().decode('utf-8').replace('\\n', '\n').lstrip(')]}\'\n')
json_content = parse(json_string)  # load the file
font_families_struct = json_content['familyMetadataList']  # get list of fonts from the file
fonts = [FontFamily(font_family_struct) for font_family_struct in font_families_struct]


def get_all_gfonts():

    return fonts
