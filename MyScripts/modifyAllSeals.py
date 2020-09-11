#! /usr/bin/python3
#! python3

import os
from tkinter import filedialog as FileDialog
from tkinter import messagebox as MessageBox
from os.path import basename
import openpyxl
import xlrd
import xlwt
from xlutils.copy import copy

#pathFile = r"S:/OPS/Marítimas/CARPETAS MOTONAVES"
pathFile = '/home/rodrigo/Downloads/'
col1 = 7
col2 = 8

def clear():  # ERASE SCREEN
    if os.name == "nt":      # Windows
        os.system("cls")
    else:
        os.system("clear")   # Linux


def getDirectory():  # DIALOG TO CHOOSE A FILE
    sealDirectory = FileDialog.askdirectory(initialdir=pathFile)
    path2 = (sealDirectory)
    # print(path2)
    return(path2)


def openDirectory(sealDirectory):  # DIALOG TO CHOOSE A FILE
    if sealDirectory != "":
        sealFiles = []
        for file in os.listdir(sealDirectory):
            sealFiles.append(file)

    # print(sealFiles)
    return(sealFiles)


def main():  # MAIN
    clear()
    path2 = getDirectory()
    sealDirectory = openDirectory(path2)  # Name of the Directory

    files = []
    for i in range(0, len(sealDirectory)):
        sealFile = (path2 + '/' + sealDirectory[i])
        # print(basename(sealFile))

        # if basename(sealFile) != 'PLANTILLA PRE-ESTIBAS.xlsx':
        (name, ext) = os.path.splitext(sealFile)  # get name and extensión
        # print(name)
        if ext == '.xls':
            # print(os.path.splitext(sealFile))
            book = xlrd.open_workbook(sealFile)
            sheet = book.sheet_by_index(1)
            book = copy(book)
            sheet2 = book.get_sheet(1)  # same sheet in order to can save

            # Loop through the sheet
            for i in range(sheet.nrows):
                sello1 = (repr(sheet.cell_value(i, 7))[1:7])
                sello2 = (repr(sheet.cell_value(i, 8)))

                if (sello2[1:3]) or (sello1[1:3])  == 'ML':
                    if sello2.find(sello1) != -1: #if there is no match equal -1
                        # background color
                        style = xlwt.easyxf(
                            'pattern: pattern solid, fore_colour yellow')
                        sheet2.write(i, 7, '0', style)  # Modify cell
                        # sheet2.write(i, 8, (sello2.replace("'", "")),
                        #             style)  # Modify cell

            files.append(sealFile)
            book.save(sealFile)  # Save
    print('Archivos procesados: ' + str(len(files)) + '\n')
    for i in range(len(files)):
        print(basename(files[i]))


if __name__ == '__main__':
    main()
