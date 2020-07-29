#! /usr/bin/python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser
import sys
import pyperclip

sys.argv  # ['mapit.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # Get address from command line.
    # ['mapit.py', '870', 'Valencia', 'St.'] => '870 Valencia St.'
    # [argument 0,  arguement 1
    address = ' '.join(sys.argv[1:])
    #                          from argument 1 en adelante
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
