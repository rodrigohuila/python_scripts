#! python3
#! /usr/bin/python3

import os
import PyPDF2
from tkinter import filedialog as FileDialog
from tkinter import messagebox as MessageBox
from os import system
from os.path import basename

path = r"D:/Users/victo/Downloads/"
path2 = r"D:/Users/victo/Desktop/RenamePDF/"
contentAll = ''


def clear():  # BORRAR PANTALLA
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def openFile(path):  # DIALOG TO CHOOSE A FILE
    pdfName = FileDialog.askopenfilename(
        initialdir=path,
        filetypes=(
            ("Archivos PDF", "*.pdf"), ("All files", "*.*")
        ),
        title="Escoja el archivo PDF a dividir."
    )
    name = basename(pdfName)
    print('\nEl nombre del archivo inicial es: ' + name + '\n')
    return(pdfName)

def pdf_splitter(pdfName, pdfReader): #SPLIT A PDF DOCUMENT
    os.chdir(path2)
    if os.path.isdir((os.path.splitext(basename(pdfName))[0])):
        MessageBox.showwarning(
            "Advertencia","""Hay una carpeta con el mismo nombre del PDF, es decir, ya se había dividido este PDF o un archivo con el mismo nombre.\n
            Los archivos se sobreescribiran""")
        #print('Advertencia:\nHay una carpeta con el mismo nombre del PDF, es decir, ya se había dividido este PDF o un archivo con el mismo nombre.\nLos archivos se sobreescribiran:\n')
        newDir = (os.path.splitext(basename(pdfName))[0])
    else:    
        os.mkdir(os.path.splitext(basename(pdfName))[0])
        newDir = (os.path.splitext(basename(pdfName))[0]) # Crear una carpeta con el mismo nombre del archivo requerido

    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter = PyPDF2.PdfFileWriter()
        pdfWriter.addPage(pageObj)
        output_filename = 'page_{}_{}'.format(
            pageNum+1, basename(pdfName))
        os.chdir(path2 + newDir) # Guardar en una carpeta con el mismo nombre del archivo requerido
        with open(output_filename, 'wb') as out:
            pdfWriter.write(out)
        print('Created: {}'.format(output_filename))            
    return(pageObj)    


def main ():
    clear ()
    pdfName = openFile(path)
    # Open the pdf file
    pdfFileObj = open( pdfName, 'rb')
    # Read info
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    pdf_splitter(pdfName, pdfReader)
    print ('\nEl documento tiene: ' + str(pdfReader.numPages) + ' páginas')
    

if __name__ == '__main__':
    main()

os.system('pause') # Press a key to continue    