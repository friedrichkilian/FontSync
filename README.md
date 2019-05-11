# Google Font Sync
This python script downloads all fonts from Google Fonts and stores them under `Library\Fonts\GoogleFonts`.

It's only compatible to macOS right now!!

## Use

There are currently 6 supported arguments:
1. [category](#category)
2. [subset](#subset)
3. [min. amount of styles (accessed via -stylecount)](#number-of-styles-accessed-via--stylecount)
4. [thickness](#thickness-slant--width)
5. [slant](#thickness-slant--width)
6. [width](#thickness-slant--width)

To use these arguments simply call them via "-[argname] [value(s)]" in the command line.
Example: "font_sync.py -category all -subset latin-ext -width 2"

#### category
Can be one of 'serif', 'sans-serif', 'display', 'handwriting' and 'monospace'.
For all styles you can use 'all', if you want to include a specific set of categories you can simply add multiple values
(like "-charset serif handwriting" for serif & handwriting)

When a category is invalid the category will be ignored (when other, valid categories are given) or taken as 'all' (if
no other valid category is given).

#### subset
Can be one of 'arabic', 'bengali', 'chinese-simplified', 'chinese-traditional', 'cyrillic', 'cyrillic-ext',
'devanagari', 'greek', 'greek-ext', 'gujarati', 'gurmukhi', 'hebrew', 'japanese', 'kannada', 'khmer', 'korean', 'latin',
'latin-ext', 'malayalam', 'myanmar', 'oriya', 'sinhala', 'tamil', 'telugu', 'thai', 'vietnamese' while 'latin-ext' is
recommended. For all subsets you can use 'all'. Wrong inputs will be taken as 'all' as well.

#### number of styles (accessed via -stylecount)

Can be a number between 2 and 18 or 'all'. All fonts which includes more or equal styles are selected. When a number
over 18 or under 2 is given, the input will be taken as 'all'.

#### thickness, slant & width

Can be a number between 1 and 10 or 'all'

## Planned updates

- [ ] gui execute in new thread & stop function
- [ ] compatibility for Windows and Linux
    - [ ] auto-detection
- [x] a GUI for simpler use
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
- [x] logging
- [ ] better logging (to file)
- [ ] auto-update
- [ ] multi-threading
- [ ] languages
- [ ] auto subset detection (is latin-ext per default in GUI)
- [ ] icon?

## Copyright
This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

You are free to:

SHARE - copy and redistribute the material in any medium or format

ADAPT - remix, transform, and build upon the material

Under the following terms:

  ATTRIBUTION - You must give appropriate credit, provide a link to the license, and indicate if changes were made.
                You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or
                your use.
                
  NONCOMMERCIAL - You may not use the material for commercial purposes.
  
  SHAREALIKE - If you remix, transform, or build upon the material, you must distribute your contributions under the
               same license as the original.
               
Follow https://creativecommons.org/licenses/by-nc-sa/4.0/ for more information.