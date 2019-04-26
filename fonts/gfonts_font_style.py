from gfonts_values import get_thickness, get_slant, get_width


class FontStyle:

    def __init__(self, id, details):

        self.id = id
        self.thickness = get_thickness(details['thickness']) if details is not None else None
        self.slant = get_slant(details['slant']) if details is not None else None
        self.width = get_width(details['width']) if details is not None else None

    def has_details(self):

        return self.thickness is None and self.slant is None and self.width is None
