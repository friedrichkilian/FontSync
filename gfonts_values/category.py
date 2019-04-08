from gfonts_values import CATEGORIES
from filter import IGNORED_KEYWORD


def get_category_list(categories):

    category_list = [Category(category) for category in categories.split(',') if category in CATEGORIES]
    return category_list if len(category_list) > 0 else IGNORED_KEYWORD


class Category:

    def __init__(self, category_id):

        self.category_id = category_id

    def __eq__(self, other):

        return self.category_id == other.category_id if isinstance(other, Category) else False
