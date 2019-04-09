from settings import get_setting
from datetime import datetime

SHOULD_PRINT = get_setting('silent_mode') is None


def log(message, type_of_message='STATUS'):

    styled_message = '[' + datetime.now().strftime('%H:%M:%S') + ' - ' + type_of_message + '] ' + message

    if SHOULD_PRINT:

        print(styled_message)
