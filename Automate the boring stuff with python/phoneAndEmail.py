#! /usr/bin/python3
# phoneAndEmail.py - Finds phones numbers and email addresses on the clipboard

import pyperclip
import re

# Create a phone regex
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 EXT 12345, ext. 12345, x12345
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   # extension
    )''', re.VERBOSE)


# Create email regex.
emailRegex = re.compile(r'''(
    # some._+thing@some.+_thing.com
    [a-zA-Z0-9._%+-]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,5})   # dot-something
    )''', re.VERBOSE)


# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


# DEBUG
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

#print(text)
#print(extractedPhone)
#print(extractedEmail)
