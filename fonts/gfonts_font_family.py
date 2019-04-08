import datetime

from settings import get_setting
from fonts.gfonts_font_style import FontStyle
from gfonts_values.category import Category
from gfonts_values.subset import get_subsets

IGNORED_KEYWORD = get_setting('keyword_all')


class FontFamily:

    def __init__(self, details):

        self.family_name = details['family']
        self.category = Category(details['category'])
        self.size = details['size']
        self.designers = details['designers']
        self.subsets = get_subsets(details['subsets'])

        date_added = details['dateAdded'].split('-')
        self.date_added = datetime.date(int(date_added[0]), int(date_added[1]), int(date_added[2]))

        last_modified = details['lastModified'].split('-')
        self.last_modified = datetime.date(int(last_modified[0]), int(last_modified[1]), int(last_modified[2]))

        self.font_styles = [FontStyle(font_style_id, font_style_details) for font_style_id, font_style_details
                            in details['fonts'].items()]
