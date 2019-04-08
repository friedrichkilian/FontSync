from gfonts_values import SUBSETS
from filter import IGNORED_KEYWORD


def get_subset(subset):

    return Subset(subset) if subset in SUBSETS else IGNORED_KEYWORD


def get_subsets(subsets):

    subset_list = [Subset(subset) for subset in subsets if subset in SUBSETS]
    return subset_list if len(subset_list) > 0 else IGNORED_KEYWORD


class Subset:

    def __init__(self, subset):

        self.subset = subset

    def __eq__(self, other):

        return self.subset == other.subset if isinstance(other, Subset) else False
