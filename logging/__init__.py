# Google Fonts Sync
# by Kilian Friedrich
#
# 2019-05-04
#
# logging/__init__.py:
#
# This script holds all the functionality which is needed for good logging:
#   1. a boolean which stores whether logging is enabled
#   2. a log(...) function which extends the builtin print() method:
#       I. The log(...) function doesn't do anything unless logging is enabled.
#       II. The time and the type of message (like 'INFO', 'STATUS', 'WARNING' etc.) are appended to the message.
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

from args.args_interface import get_bool
from datetime import datetime

SHOULD_PRINT = not get_bool('silent-mode')  # set SHOULD_PRINT to false when silent mode is activated


# This sould ALWAYS be called instead of print() so that silent mode can work
def log(message, type_of_message='STATUS', lbl=None):

    if lbl is not None:

        lbl[1].set(message)

    # print only when silent mode is disabled
    if SHOULD_PRINT:

        # just new line if message is empty
        if message == '':

            print()
            return

        # style the message (add '[HH:MM:SS] ')
        styled_message = '[' + datetime.now().strftime('%H:%M:%S') + ' - ' + type_of_message + '] ' + message

        print(styled_message)
