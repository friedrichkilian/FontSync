# Google Fonts Sync
# by Kilian Friedrich
#
# 2019-05-04
#
# gui/main_frame.py:
#
# This script builds a frame and holds all necessary functions & variables.
# The frame is a collection of all possible filters and buttons (to start the syncing process and to open settings (not
# implemented yet).
# All these filters got there global variables which stores their state. This is necessary so that the
# __execute_sync__() function can access the selected filters. __execute_sync__() is called via a press on the 'Sync'
# button in the frame.
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

from tkinter import Tk, Frame, Label, Button, Checkbutton, OptionMenu, Scale, StringVar, IntVar, BooleanVar
from re import sub

from gfonts_values import CATEGORIES, SUBSETS
from font_sync import sync

# stores which checkboxes are checked
category_checkbox_values = dict()

# stores selected subset and list of available subsets
subset_options = dict()  # keys are readable options, values are ids
subset_selected = None

# stores stylecount stuff
apply_stylecount = None
stylecount = None

# stores thickness stuff
apply_thickness = None
thickness = None

# stores slant stuff
apply_slant = None
slant = None

# stores width stuff
apply_width = None
width = None


# builds the frame
def create_frame():

    # create frame
    master = Tk()
    master.title('Google Fonts Sync by kilianfriedrich')  # set title

    # set size
    master.geometry('710x300')
    master.resizable(width=False, height=False)  # don't make it resizable bc it's not responsive

    # ===== CATEGORY SECTION ===== #
    category_frame = Frame(master, highlightbackground='black', highlightthickness=1)  # create frame for category stuff

    # add label
    Label(category_frame, text='Select categories to download').place(x=10, y=10)

    # add every category from CATEGORIES
    y = 10  # stores vertical position of current checkbox
    for category in CATEGORIES:

        y += 20  # change position

        # add BooleanVar() to category_checkbox_values which stores whether the checkbox is checked
        category_checkbox_values[category] = BooleanVar()
        category_checkbox_values[category].set(True)  # set it to True

        # construct category title of its id
        # id is like: sans-serif
        # title should be: Sans Serif
        # So these are the steps:
        #   1. replace '-' by ' '
        #   2. make every word start with a capital
        category_name = sub(r'\b[a-z]', lambda s: s.group().upper(), category.replace('-', ' '))

        # add actual checkbox
        Checkbutton(category_frame, text=category_name, variable=category_checkbox_values[category],
                    onvalue=True, offvalue=False,
                    command=lambda: __toggle_checkbox__()).place(x=10, y=y)

    category_frame.config(width=230, height=y+30)  # set frames size
    category_frame.place(x=10, y=10)  # add frame to window

    # ===== SUBSET SECTION ===== #
    subset_frame = Frame(master, highlightbackground='black', highlightthickness=1)  # create frame for subset stuff

    # add label
    Label(subset_frame, text='Select included subset').place(x=10, y=10)

    global subset_selected  # access global variable
    subset_selected = StringVar()  # create a StringVar to store currently selected subset

    # iterate through available subsets
    for subset in SUBSETS:

        # construct subset title of id
        # id be like: latin-ext
        # title should be: Latin (Extended)
        # So these are the steps:
        #   1. replace '-' by ' '
        #   2. make every word start with a capital letter
        #   3. surround every second word (words with space in front of them) with '(' and ')'
        #   4. replace 'Ext' to 'Extended' if 'Ext' is in the string
        # DON'T TOUCH IT
        subset_name = sub(' [A-Z][a-z]+', lambda s: ' (' + s.group().lstrip().replace('Ext', 'Extended') + ')',
                          sub(r'\b[a-z]', lambda s: s.group().upper(), subset.replace('-', ' ')))
        subset_options[subset_name] = subset  # store it

    # create subset dropdown list
    subset_dropdown = OptionMenu(subset_frame, subset_selected, 'All subsets', *subset_options)
    subset_dropdown.place(x=10, y=30)  # place it

    subset_frame.config(width=200, height=60)  # set frame sizes
    subset_frame.place(x=250, y=10)  # add frame to window

    # ===== STYLECOUNT SECTION ===== #
    stylecount_frame = Frame(master, highlightbackground='black', highlightthickness=1)  # create frame for this stuff

    # add label
    Label(stylecount_frame, text='Min. amount of styles per font').place(x=10, y=10)

    global apply_stylecount  # access global variable
    apply_stylecount = BooleanVar()  # create BooleanVar to store whether this filter should be applied
    # add checkbox to select whether the filter should be applied
    Checkbutton(stylecount_frame, text='Apply this filter', variable=apply_stylecount, onvalue=True, offvalue=False)\
        .place(x=10, y=30)

    global stylecount  # access global variable
    stylecount = IntVar()  # create IntVar to store value of following slider:
    # create slider for the filter
    Scale(stylecount_frame, from_=2, to=10, orient='horizontal', variable=stylecount).place(x=10, y=50)
    # set frame sizes
    stylecount_frame.config(width=220, height=100)  # set frame sizes
    stylecount_frame.place(x=250, y=80)  # add frame to window

    # ===== THICKNESS SECTION ===== #
    thickness_frame = Frame(master, highlightbackground='black', highlightthickness=1)

    # add label
    Label(thickness_frame, text='Thickness').place(x=10, y=10)

    global apply_thickness  # access global variable
    apply_thickness = BooleanVar()  # create BooleanVar to store whether this filter should be applied
    # add checkbox to select whether the filter should be applied
    Checkbutton(thickness_frame, text='Apply this filter', variable=apply_thickness, onvalue=True, offvalue=False) \
        .place(x=10, y=30)

    global thickness  # access global variable
    thickness = IntVar()  # create IntVar to store value of following slider:
    # create slider for the filter
    Scale(thickness_frame, from_=1, to=10, orient='horizontal', variable=thickness).place(x=10, y=50)

    thickness_frame.config(width=220, height=100)  # set frame sizes
    thickness_frame.place(x=480, y=80)  # add frame to window

    # ===== SLANT SECTION ===== #
    slant_frame = Frame(master, highlightbackground='black', highlightthickness=1)

    # add label
    Label(slant_frame, text='Slant').place(x=10, y=10)

    global apply_slant  # access global variable
    apply_slant = BooleanVar()  # create BooleanVar to store whether this filter should be applied
    # add checkbox to select whether the filter should be applied
    Checkbutton(slant_frame, text='Apply this filter', variable=apply_slant, onvalue=True, offvalue=False) \
        .place(x=10, y=30)

    global slant  # access global variable
    slant = IntVar()  # create IntVar to store value of following slider:
    # create slider for the filter
    Scale(slant_frame, from_=1, to=10, orient='horizontal', variable=slant).place(x=10, y=50)

    slant_frame.config(width=220, height=100)  # set frame sizes
    slant_frame.place(x=250, y=190)  # add frame to window

    # ===== WIDTH SECTION ===== #
    width_frame = Frame(master, highlightbackground='black', highlightthickness=1)

    # add label
    Label(width_frame, text='Width').place(x=10, y=10)

    global apply_width  # access global variable
    apply_width = BooleanVar()  # create BooleanVar to store whether this filter should be applied
    # add checkbox to select whether the filter should be applied
    Checkbutton(width_frame, text='Apply this filter', variable=apply_width, onvalue=True, offvalue=False) \
        .place(x=10, y=30)

    global width  # access global variable
    width = IntVar()  # create IntVar to store value of following slider:
    # create slider for the filter
    Scale(width_frame, from_=1, to=10, orient='horizontal', variable=width).place(x=10, y=50)

    width_frame.config(width=220, height=100)  # set frame sizes
    width_frame.place(x=480, y=190)  # add frame to window

    # ===== SYNC BUTTON SECTION ===== #
    # create a frame for the button
    # this is needed for the following reason:
    #   the size of a button can't be set in pixels
    #   a frame's size can be set in pixels
    #   -> let the button fill the frame
    # this makes the button look bad but that's ok
    button_frame = Frame(master, width=230, height=30)
    button_frame.pack_propagate(0)  # don't let the frame resize itself

    button = Button(button_frame, text='Sync!')  # create button
    # add target function
    # this could be done without lambda:... but this results in the fact that __execute_sync__() is called before the
    # button is pressed
    button.config(command=lambda: __execute_sync__())

    button.pack(fill='both', expand=1)  # let the btton expand
    button_frame.place(x=10, y=260)  # place the frame

    # ===== FINISH ===== #
    master.mainloop()  # make the window visible


# this will be called when a checkbox was enabled/disabled and makes sure that at least one checkbox is always checked
def __toggle_checkbox__():

    # if amount of checked checkboxes is zero
    if len([val for val in category_checkbox_values.values() if val.get()]) == 0:

        [val.set(True) for val in category_checkbox_values.values()]  # enable it again


# syncs
# make sure this is never called when no frame is cerated before!
def __execute_sync__():

    # collect inputs
    categories = [category for category in category_checkbox_values.keys()
                  if category_checkbox_values[category].get()]
    subset = subset_options.get(subset_selected.get(), '')
    stylecount_value = stylecount.get() if apply_stylecount.get() else 0
    thickness_value = thickness.get() if apply_thickness.get() else 0
    slant_value = slant.get() if apply_slant.get() else 0
    width_value = width.get() if apply_width.get() else 0

    # call font_sync -> sync()
    sync(categories, subset, stylecount_value, thickness_value, slant_value, width_value)
