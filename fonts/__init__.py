# Google Fonts Sync
# by Kilian Friedrich
#
# 2019-04-28
#
# fonts/__init__.py:
#
# This script downloads information of all fonts and returns them in get_all_gfonts()

from json import loads as parse  # is used to parse Google's JSON file about their fonts
from urllib.request import urlopen as fetch_internet_file  # is used to download Google's JSON file about their fonts

from fonts.gfonts_font_family import FontFamily

JSON_DOWNLOAD_URL = 'https://fonts.google.com/metadata/fonts'  # the JSON file is stored here


def get_all_gfonts():

    json_download = fetch_internet_file(JSON_DOWNLOAD_URL)  # fetch Google's JSON

    # Google's JSON is weirdly encoded, has escaped line breaks and begins with ')]}'' for some reason
    # this line will convert the JSON to a readable file
    json_string = json_download.read().decode('utf-8').replace('\\n', '\n').lstrip(')]}\'\n')
    json_content = parse(json_string)  # load the file
    font_families_struct = json_content['familyMetadataList']  # get list of fonts from the file
    return [FontFamily(font_family_struct) for font_family_struct in font_families_struct]
