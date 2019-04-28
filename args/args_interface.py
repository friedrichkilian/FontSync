from args import arg_values, arg_booleans


def get_bool(bool_title):

    return bool(arg_values.get(bool_title, bool_title in arg_booleans))


def get_str(str_title):

    return str(arg_values.get(str_title, str_title in arg_booleans))


def get_list(list_title):

    value = arg_values.get(list_title, None)
    if not isinstance(value, list):

        value = [value]

    return list(value) if value is not None else list()


def get_int(int_title):

    return int(arg_values.get(int_title, int_title in arg_booleans))