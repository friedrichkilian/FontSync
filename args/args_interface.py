# Google Fonts Sync
# by Kilian Friedrich
#
# 2019-04-28
#
# args/args_interface.py:
#
# This script is an interface to the command line arguments
# Although the contents (which were collected in args/__init__.py) can be directly accessed this set of methods should
# make it easier to handle.
#
# Supported data types:
#   booleans (via get_bool(...)) - will search through collected booleans (arg_booleans from args/__init__.py) and
#                                  return True if the given boolean was found
#   strings (via get_str(...))   - will return the list as string, the entries will be separated by commas
#                                  returns '' if the key wasn't found
#   lists (via get_list(...))    - will return the values as they are stored in arg_values (from args/__init__.py)
#                                  returns [] if the key wasn't found
#   integer (via get_int(...))   - will return (the first) value assigned to the key which can be casted to an integer
#                                  returns NaN if there is no castable content
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

from args import ARG_V, ARG_B  # arguments are stored here
from math import nan  # NaN will be returned when an integer is required but not existent


# will search through collected booleans (arg_booleans from args/__init__.py)
# returns True if the given boolean was found
def get_bool(key):

    return key in ARG_B


# will return the list as string, the entries will be separated by commas
# returns '' if the key was not found
def get_str(key):

    string = ''  # the strng which will be returned later
    # iterate through values
    # or through an empty list if the key wasn't found (results in empty string since it doesn't loop)
    for entry in ARG_V.get(key, []):

        string += str(entry) + ','  # add value + comma to the string

    return string.rstrip(',')  # removes the last comma and returns the string


# will return he values as they are stored un arg_values (from args/__init__.py)
# return [] if the key wasn't found
def get_list(key):

    return ARG_V.get(key, [])


# will return the nth value assigned to the key which can be casted to an integer
# returns NaN if there is no castable content
def get_int(key, n=1):

    # collect every integer which is found in the values, uses an empty list if the key was not found
    integers = [int(entry) for entry in ARG_V.get(key, []) if entry.lstrip('-').isdigit()]

    # return the nth found integer, if n is out of range return the first integer, if no integer was catched return NaN
    return integers[n - 1] if n in range(1, len(integers) + 1) else integers[0] if len(integers) > 0 else nan
