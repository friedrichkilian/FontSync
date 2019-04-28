# Google Fonts Sync
# by Kilian Friedrich
#
# 2019-04-28
#
# args/__init__.py:
#
# This script will parse arguments from the user.
# Supported arguments:
#   --[...]      -> a boolean,
#                   no further values are expected
#   -[...] [...] -> a key,
#                   values after such arguments are taken as its contents
#
# Other passed arguments are ignored!

from sys import argv  # arguments which are passed on the command line are stored in this 'argv' array

arg_values = dict()  # stores values
arg_booleans = list()  # stores booleans

__cur_key__ = None  # stores the name of the current value so that contents can be added to it
for arg in argv:

    if arg.startswith('--'):

        __cur_key__ = None  # clear current value
        arg_booleans.append(arg.lstrip('--'))  # add argument to (global) list of booleans

    elif arg.startswith('-'):

        __cur_key__ = arg.lstrip('-')
        arg_values[__cur_key__] = list()  # adds key to dict & assigns an empty list (/clears entry if already there)

    # argument is neither a boolean nor a key
    # just continue if there is a current key to assign the value to
    elif __cur_key__ is not None:

        arg_values[__cur_key__].append(arg)  # appends value to key
