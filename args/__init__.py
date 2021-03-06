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
# Other passed arguments are ignored!
#
# Copyright after CC BY-NC-SA 4.0
# You are free to:
#   SHARE - copy and redistribute the material in any medium or format
#   ADAPT - remix, transform, and build upon the material
# Under the following terms:
#   ATTRIBUTION - You must give appropriate credit, provide a link to the license, and indicate if changes were made.
#                 You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or
#                 your use.
#   NONCOMMERCIAL - You may not use the material for commercial purposes.
#   SHAREALIKE - If you remix, transform, or build upon the material, you must distribute your contributions under the
#                same license as the original.
# Follow https://creativecommons.org/licenses/by-nc-sa/4.0/ for more information.

from sys import argv  # arguments which are passed on the command line are stored in this 'argv' array

ARG_V = dict()  # stores values
ARG_B = list()  # stores booleans

__cur_key__ = None  # stores the name of the current value so that contents can be added to it
for arg in argv:

    if arg.startswith('--'):

        __cur_key__ = None  # clear current value
        ARG_B.append(arg.lstrip('--'))  # add argument to (global) list of booleans

    elif arg.startswith('-'):

        __cur_key__ = arg.lstrip('-')
        ARG_V[__cur_key__] = list()  # adds key to dict & assigns an empty list (/clears entry if already there)

    # argument is neither a boolean nor a key
    # just continue if there is a current key to assign the value to
    elif __cur_key__ is not None:

        ARG_V[__cur_key__].append(arg)  # appends value to key
