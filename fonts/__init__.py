from json import loads as parse
from urllib.request import urlopen as download

from settings import get_setting
from fonts.gfonts_font_family import FontFamily

JSON_DOWNLOAD_URL = get_setting('gfonts_url_json')


def get_fonts():

    json_download = download(JSON_DOWNLOAD_URL)
    json_string = json_download.read().decode('utf-8').replace('\\n', '\n').lstrip(')]}\'\n')
    json_content = parse(json_string)
    font_families_struct = json_content['familyMetadataList']
    fonts = [FontFamily(font_family_struct) for font_family_struct in font_families_struct]

    return fonts
