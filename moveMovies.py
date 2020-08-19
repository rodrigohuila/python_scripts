#! /usr/bin/python3

import os
import shutil

home = '/home/rodrigo/'

for folderName, subfolders, filenames in os.walk(home + 'Downloads'):
    for file in filenames:
        if file.endswith('.mp4'):
            shutil.move(home + 'Downloads/' + file, home + 'Videos/Movies/')
            print ('\nThe file' + home + 'Downloads/' + file + 'was moved')
            empty = 'false'
        else:
            empty = 'true'   

if empty == ('true'):
    print('\nThere is not any file with .mp4 extension') 