from tkinter import Tk, Frame, Label, Button, Checkbutton, OptionMenu, Scale, StringVar, IntVar, BooleanVar
from re import sub

from gfonts_values import CATEGORIES, SUBSETS
from font_sync import sync

category_checkbox_values = dict()

subset_options = dict()
subset_selected = None

apply_stylecount = None
stylecount = None

apply_thickness = None
thickness = None

apply_slant = None
slant = None

apply_width = None
width = None


def create_frame():

    master = Tk()
    master.title('Google Fonts Sync by kilianfriedrich')

    master.geometry('710x300')
    master.resizable(width=False, height=False)

    category_frame = Frame(master, highlightbackground='black', highlightthickness=1)

    Label(category_frame, text='Select categories to download').place(x=10, y=10)

    y = 10
    for category in CATEGORIES:

        y += 20
        category_checkbox_values[category] = BooleanVar()
        category_checkbox_values[category].set(False)

        category_name = sub(r'\b[a-z]', lambda s: s.group().upper(), category.replace('-', ' '))
        Checkbutton(category_frame, text=category_name, variable=category_checkbox_values[category], onvalue=True,
                    offvalue=False).place(x=10, y=y)

    category_frame.config(width=230, height=y+30)
    category_frame.place(x=10, y=10)

    subset_frame = Frame(master, highlightbackground='black', highlightthickness=1)

    Label(subset_frame, text='Select included subset').place(x=10, y=10)

    global subset_selected
    subset_selected = StringVar()
    subset_selected.set('Latin (Extended)')

    for subset in SUBSETS:

        subset_name = sub(' [A-Z][a-z]+', lambda s: ' (' + s.group().lstrip().replace('Ext', 'Extended') + ')',
                          sub(r'\b[a-z]', lambda s: s.group().upper(), subset.replace('-', ' ')))
        subset_options[subset_name] = subset

    subset_dropdown = OptionMenu(subset_frame, subset_selected, 'All subsets', *subset_options)
    subset_dropdown.place(x=10, y=30)

    subset_frame.config(width=200, height=60)
    subset_frame.place(x=250, y=10)

    stylecount_frame = Frame(master, highlightbackground='black', highlightthickness=1)

    Label(stylecount_frame, text='Min. amount of styles per font').place(x=10, y=10)

    global apply_stylecount
    apply_stylecount = BooleanVar()
    Checkbutton(stylecount_frame, text='Apply this filter', variable=apply_stylecount, onvalue=True, offvalue=False)\
        .place(x=10, y=30)

    global stylecount
    stylecount = IntVar()
    Scale(stylecount_frame, from_=2, to=10, orient='horizontal', variable=stylecount).place(x=10, y=50)

    stylecount_frame.config(width=220, height=100)
    stylecount_frame.place(x=250, y=80)

    thickness_frame = Frame(master, highlightbackground='black', highlightthickness=1)

    Label(thickness_frame, text='Thickness').place(x=10, y=10)

    global apply_thickness
    apply_thickness = BooleanVar()
    Checkbutton(thickness_frame, text='Apply this filter', variable=apply_thickness, onvalue=True, offvalue=False) \
        .place(x=10, y=30)

    global thickness
    thickness = IntVar()
    Scale(thickness_frame, from_=1, to=10, orient='horizontal', variable=thickness).place(x=10, y=50)

    thickness_frame.config(width=220, height=100)
    thickness_frame.place(x=480, y=80)

    slant_frame = Frame(master, highlightbackground='black', highlightthickness=1)

    Label(slant_frame, text='Slant').place(x=10, y=10)

    global apply_slant
    apply_slant = BooleanVar()
    Checkbutton(slant_frame, text='Apply this filter', variable=apply_slant, onvalue=True, offvalue=False) \
        .place(x=10, y=30)

    global slant
    slant = IntVar()
    Scale(slant_frame, from_=1, to=10, orient='horizontal', variable=slant).place(x=10, y=50)

    slant_frame.config(width=220, height=100)
    slant_frame.place(x=250, y=190)

    width_frame = Frame(master, highlightbackground='black', highlightthickness=1)

    Label(width_frame, text='Width').place(x=10, y=10)

    global apply_width
    apply_width = BooleanVar()
    Checkbutton(width_frame, text='Apply this filter', variable=apply_width, onvalue=True, offvalue=False) \
        .place(x=10, y=30)

    global width
    width = IntVar()
    Scale(width_frame, from_=1, to=10, orient='horizontal', variable=width).place(x=10, y=50)

    width_frame.config(width=220, height=100)
    width_frame.place(x=480, y=190)

    button_frame = Frame(master, width=230, height=30)
    button_frame.pack_propagate(0)

    button = Button(button_frame, text='Sync!')
    button.config(command=lambda: __execute_sync__())

    button.pack(fill='both', expand=1)
    button_frame.place(x=10, y=260)

    master.mainloop()


def __execute_sync__():

    categories = [category for category in category_checkbox_values.keys()
                  if category_checkbox_values[category].get()]
    subset = subset_options.get(subset_selected.get(), '')
    stylecount_value = stylecount.get() if apply_stylecount.get() else 0
    thickness_value = thickness.get() if apply_thickness.get() else 0
    slant_value = slant.get() if apply_slant.get() else 0
    width_value = width.get() if apply_width.get() else 0

    sync(categories, subset, stylecount_value, thickness_value, slant_value, width_value)
