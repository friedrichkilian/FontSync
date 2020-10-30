# Google Font Sync (Python 3.9.0)
This python script downloads all fonts from Google Fonts and installs them (/moves them in the font folder of the OS).

## Known Bugs
- Target Directory Selection doesn't work on macOS (that's a python bug)

## How to use

There are currently 6 supported arguments:
1. [category](#category)
2. [subset](#subset)
3. [min. amount of styles (-stylecount)](#number-of-styles-accessed-via--stylecount)
4. [thickness](#thickness-slant--width)
5. [slant](#thickness-slant--width)
6. [width](#thickness-slant--width)

To use these arguments simply call them via "-[argname] [value(s)]" in the command line.
Example: "font_sync.py -category all -subset latin-ext -width 2"

#### category
`serif`, `sans-serif`, `display`, `handwriting` or `monospace`.<br>
Default:  `all`.

You may also include multiple values:<br>
`font_sync.py -category serif handwriting`

Invalid categories are ignored.

#### subset
`arabic`, `bengali`, `chinese-simplified`, `chinese-traditional`, `cyrillic`, `cyrillic-ext`,
`devanagari`, `greek`, `greek-ext`, `gujarati`, `gurmukhi`, `hebrew`, `japanese`, `kannada`, `khmer`, `korean`, `latin`,
`latin-ext`, `malayalam`, `myanmar`, `oriya`, `sinhala`, `tamil`, `telugu`, `thai`, or `vietnamese`.<br>

Invalid subsets are ignored.

#### number of styles (-stylecount)
Between `2` and `10`.<br>
Default: `all`.

All fonts with so many or more styles are selected.<br>
Invalid inputs are ignored.

#### thickness, slant & width
Between `1` and `10`.<br>
Default: `all`.

Invalid inputs are ignored.

## TO-DOs

- [x] gui execute in new thread & stop function
- [x] compatibility for Windows and Linux -> profiles
    - [x] auto-detection
- [x] a GUI for simpler use
- [ ] autostart function
- [ ] option to delete fonts which aren't longer in Google's database
- [ ] skip fonts which are already installed
- [ ] more filter options (exact number of styles/max number of styles/one font)
- [ ] only fitting styles of a font
- [x] logging
- [ ] better logging (to file)
- [ ] max. amount of fonts
- [x] optimize files

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
