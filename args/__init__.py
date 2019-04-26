from sys import argv

arg_values = dict()
arg_booleans = list()

value_name = None
for arg in [str(argument) for argument in argv]:

    if arg.startswith('--'):

        value_name = None
        arg_booleans.append(arg.lstrip('--'))
        continue

    if arg.startswith('-'):

        value_name = arg.lstrip('-')
        arg_values[value_name] = None
        continue

    if value_name is not None:

        if arg_values[value_name] is None:

            arg_values[value_name] = arg

        elif isinstance(arg_values[value_name], str):

            arg_values[value_name] = [arg_values[value_name], arg]

        else:

            arg_values[value_name].append(arg)
