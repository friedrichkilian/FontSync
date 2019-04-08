import ssl as https_config
from sys import argv as arguments
from urllib import request as internet
from glob import glob as get_files
from zipfile import ZipFile as ZIPFile
from os import makedirs as make_dir, remove as remove_file

from settings import get_setting
from fonts import get_fonts

from gfonts_values.category import get_category_list
from gfonts_values.subset import get_subset
from gfonts_values.stylecount import get_stylecount
from gfonts_values.thickness import get_thickness
from gfonts_values.slant import get_slant
from gfonts_values.width import get_width

from filter.gfonts_filter import filter_fonts

IGNORED_KEYWORD = get_setting('keyword_all')


def sync(category_arg, subset_arg, stylecount_arg, thickness_arg, slant_arg, width_arg):

    category_list = get_category_list(category_arg)
    subset = get_subset(subset_arg)
    stylecount = get_stylecount(stylecount_arg)
    thickness = get_thickness(thickness_arg)
    slant = get_slant(slant_arg)
    width = get_width(width_arg)

    for font_family in filter_fonts(get_fonts(), category_list, subset, stylecount, thickness, slant, width):

        dir_name = font_family.family_name.replace(' ', get_setting('output_dir_space_replacement'))
        dir_path = get_setting('output_dir').format(dir_name)
        zip_path = dir_path + '.zip'

        download_name = font_family.family_name.replace(' ', get_setting('gfonts_url_download_space_replacement'))
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
