# Google Font Sync #
This python script downloads all fonts from Google Fonts and stores them under `Library\Fonts\GoogleFonts`.

It's only compatible to macOS right now!!

## Use ##

You can use Google Font sync with either 6 or 0 arguments (everything else will be counted as no arguments).
These arguments are:
1. [category](#category)
2. [supported subset](#subset)
3. [min. amount of styles](#number-of-styles)
4. [thickness](#thickness-slant--width)
5. [slant](#thickness-slant--width)
6. [width](#thickness-slant--width)

#### category ####
Can be one of 'serif', 'sans-serif', 'display', 'handwriting' and 'monospace'.
For all styles you can use 'all', for a few you can seperate two or more of them via comma
(e.g. 'serif,sans-serif,monospace').

When a category is invalid the category will be ignored (when other, valid categories are given) or taken as 'all' (if
no other valid category is given).

#### subset ####
Can be one of 'arabic', 'bengali', 'chinese-simplified', 'chinese-traditional', 'cyrillic', 'cyrillic-ext',
'devanagari', 'greek', 'greek-ext', 'gujarati', 'gurmukhi', 'hebrew', 'japanese', 'kannada', 'khmer', 'korean', 'latin',
'latin-ext', 'malayalam', 'myanmar', 'oriya', 'sinhala', 'tamil', 'telugu', 'thai', 'vietnamese' while 'latin-ext' is
recommended. For all subsets you can use 'all'.

You cannot separate two or more via comma! Wrong inputs will be taken as 'all'.

#### number of styles ####

Can be a number between 2 and 18 or 'all'. All fonts which includes more or equal styles are selected. When a number
over 18 or under 2 is given, the input will be taken as 'all'.

#### thickness, slant & width ####

Can be a number between 1 and 10 or 'all'

## Planned updates ##

- [ ] compatibility for Windows and Linux
    - [ ] auto-detection
    - [ ] .exe for Windows / .App for macOS / .py and .deb for Linux
- [ ] a GUI for simpler use
- [ ] an installation utility
    - [ ] an uninstallation utility
- [ ] autostart function
- [ ] option to delete fonts which aren't longer in Google's database
- [ ] skip fonts which are already installed
- [ ] be able to install fonts only for users
    - [ ] be able to install fonts without folders for each font
    - [ ] be able to install fonts in custom directory
- [ ] more filter options (exact number of styles/max number of styles/one font)
- [ ] install only fitting styles of a font
- [ ] compatibility to other font services like Adobe Fonts
- [ ] logging
- [ ] auto-update