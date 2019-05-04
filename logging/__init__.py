# Google Fonts Sync
# by Kilian Friedrich
#
# 2019-05-04
#
# logging/__init__.py:
#
# This script includes functions for logging

from args.args_interface import get_bool
from datetime import datetime

SHOULD_PRINT = not get_bool('silent-mode')  # set SHOULD_PRINT to false when silent mode is activated


# This sould ALWAYS be called instead of print() so that silent mode can work
def log(message, type_of_message='STATUS'):

    # style the message (add '[HH:MM:SS] ')
    styled_message = '[' + datetime.now().strftime('%H:%M:%S') + ' - ' + type_of_message + '] ' + message

    # print only when silent mode is disabled
    if SHOULD_PRINT:

        print(styled_message)
