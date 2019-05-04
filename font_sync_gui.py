# Google Fonts Sync
# by Kilian Friedrich
#
# 2019-05-04
#
# font_sync_gui.py:
#
# This script just calls one method (create_frame() from gui/main_frame.py)
# it exists so that gui/main_frame.py -> create_frame() can be accessed easier, but you could call it directly too

from gui import main_frame

main_frame.create_frame()  # create frame
