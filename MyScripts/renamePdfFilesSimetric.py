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


def openFile():  # DIALOG TO CHOOSE A FILE
    pdfName = FileDialog.askopenfilename(
        initialdir=path,
        filetypes=(('pdf', '*.pdf'), ('all files', '*.*')),
        title='Escoja el archivo de imagen a dividir y renombrar'
    )
    name = basename(pdfName)
    print('\nEl nombre del archivo inicial es: ' + name + '\n')
    return(pdfName)


def pdf_splitter(pdfName, pdfReader): #SPLIT PDF FILE
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter = PyPDF2.PdfFileWriter()
        pdfWriter.addPage(pageObj)
        finalName = extract_text(pdfReader, pageNum)  #Enviar pdf para extraer texto
        output_filename = '{}.pdf'.format(
            finalName)
        os.chdir(path2)
        with open(output_filename, 'wb') as out:
            pdfWriter.write(out)
        print('Created: {}'.format(output_filename))
        #finalName = extract_text(pdfReader, pageNum)  #Enviar pdf para extraer texto


def extract_text(pdfReader, pageNum): # EXTRACT TEXT FROM PDF FILE
    pageObj = pdfReader.getPage(pageNum)  # Read the content of the first page
    cadena = pageObj.extractText()
    #print ('\nEl contenido de la página No: ' + str(pageNum) + 'del PDF es el siguiente: \n' + content)
    #return(content)
    finalName = read_texto(cadena)
    return(finalName)


def read_texto(cadena):  # READ THE ESPECIFIC SRRING THAT WE NEED
    startWord = cadena.index(
        'Señor (a)')  # Ingresamos el texto inicial de la búsqueda
    # Ingresamos el texto final de la búsqueda
    endWord = cadena.index('La Directora ')

    subcadena = cadena[startWord:endWord].replace('\n', ' ').replace('Señor', '')
    #newString = subcadena.replace('\n', ' ')
    subcadena = subcadena.split(' ')  # Split string to capitalize word by word
        
    finalName = []
    for word in subcadena:
        if len(word) > 2 and (word.isalpha() == True):
            finalName.append(word.capitalize())
        elif len(word) <= 2 and (word.isalpha() == True):
            finalName.append(word.lower())
        elif len(word) > 2 and (word.isdigit() == True):
            word2 = 'CC_' + word
            finalName.append(word2)

    finalName = '_'.join(finalName)
    return(finalName)
    


def main():
    clear()
    pdfName = openFile() # Open the pdf file
    pdfFileObj = open( pdfName, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) # Read info
    pdf_splitter(pdfName, pdfReader)
    print ('\nFueron Procesadas: ' + str(pdfReader.numPages) + ' páginas')
    
        
if __name__ == '__main__':
    main()    
    
os.system('pause') # Press a key to continue        