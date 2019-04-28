import ssl as https_config
from urllib import request as internet
from glob import glob as get_files
from zipfile import ZipFile as ZIPFile
from os import makedirs as make_dir, remove as remove_file

from logging import log
from settings import get_setting
from fonts import get_fonts
from filter.gfonts_filter import filter_fonts
from gfonts_values import get_category_list, get_subset, get_stylecount, get_thickness, get_slant, get_width
from args import args_interface as args


def sync(category_arg, subset_arg, stylecount_arg, thickness_arg, slant_arg, width_arg):

    category_list = get_category_list(category_arg)
    subset = get_subset(subset_arg)
    stylecount = get_stylecount(stylecount_arg)
    thickness = get_thickness(thickness_arg)
    slant = get_slant(slant_arg)
    width = get_width(width_arg)

    for font_family in filter_fonts(get_fonts(), category_list, subset, stylecount, slant, thickness, width):

        dir_name = font_family.family_name.replace(' ', get_setting('output_dir_space_replacement'))
        dir_path = get_setting('output_dir').format(dir_name)
        zip_path = dir_path + '.zip'

        download_name = font_family.family_name.replace(' ', get_setting('gfonts_url_download_space_replacement'))
        download_url = get_setting('gfonts_url_download').format(download_name)

        log('Downloading ' + font_family.family_name + ' from ' + download_url + ' to ' + zip_path + '...')
        internet.urlretrieve(download_url, zip_path)
        zip_file = ZIPFile(zip_path, 'r')

        log('Clearing ' + dir_path + '/*...')
        make_dir(dir_path, exist_ok=True)
        files = get_files(zip_path + '/*')
        for f in files:
            remove_file(f)

        log('Extracting ' + zip_path + '...')
        zip_file.extractall(dir_path)
        log('Deleting ' + zip_path + '...')
        remove_file(zip_path)


# noinspection PyProtectedMember
https_config._create_default_https_context = https_config._create_unverified_context
make_dir('/Library/Fonts/GoogleFonts', exist_ok=True)

if __name__ == '__main__':
    sync(args.get_list('category'), args.get_str('subset'), args.get_int('stylecount'), args.get_int('thickness'),
         args.get_int('slant'), args.get_int('width'))
