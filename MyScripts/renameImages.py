#! /usr/bin/python3

try:
    from PIL import Image
except ImportError:
    import Image
from pdf2image import convert_from_path
import img2pdf
from PIL import Image
import pytesseract
import os
import shutil
import zipfile
from tkinter import filedialog as FileDialog
from tkinter import messagebox as MessageBox
from os import system
from os.path import basename

pathFile = '/home/rodrigo/Downloads/Victoria/' # Directory for the final files
ext = 'jpg' # File Ext


def clear():  # ERASE SCREEN
    if os.name == "nt":      # Windows
        os.system("cls")
    else:
        os.system("clear")   # Linux


def openFile():  # DIALOG TO CHOOSE A FILE
    imageName = FileDialog.askopenfilename(
        initialdir='/home/rodrigo/Downloads/',
        filetypes=(('pdf', '*.pdf'), ('all files', '*.*')),
        title='Escoja el archivo de imagen a dividir y renombrar'
    )
    print('\nEl nombre del archivo inicial es: ' + basename(imageName) + '\n')
    return(imageName)


def convert_image(imageName, pathFile, ext):  # CONVERT IMAGEN TO A SELECT EXT
    lstFiles = []
    convert_from_path(imageName, output_folder=pathFile,
                      fmt=ext, output_file='Diploma')

    for fichero in os.listdir(pathFile):
        (nombreFichero, extension) = os.path.splitext(fichero)
        if(extension == "." + ext):
            lstFiles.append(nombreFichero+extension)
    return(lstFiles)


def ocr_core(fileName):  # OCR PROCESSING OF IMAGES
    text = pytesseract.image_to_string(Image.open(
        fileName))  # Pillow's Image class open image and pytesseract detect strings
    return text


def read_image(cadena):  # READ LETTERS AND STRINGS IN THE IMAGE WITH GOOGLE OCR
    startWord = cadena.index(
        'CERTIFICA')  # Initial text for the search
    endWord = cadena.index('CON UNA') # Final text for the search

    subcadena = cadena[startWord:endWord]
    newString = subcadena.lstrip("CERTIFICA QUE").lstrip("CERTIFICA").lstrip(
        "QUE").lstrip(':').replace('\n', ' ').replace('.', '').replace('ASISTIO Y APROBO EL CURSO DE', 'Curso de').strip().rstrip("CON UN").rstrip().rstrip().replace(' ', '_').lower()

    newString = newString.split('_')  # Split string to capitalize word by word
    newString2 = []
    for word in newString:
        if len(word) > 2:
            newString2.append(word.capitalize())
        else:
            newString2.append(word)
    newString2 = '_'.join(newString2)
    return(newString2)


def rename_file(name, finalName):  # RENAME FILES
    archivo = name
    nombreNuevo = (finalName + "." + ext)
    os.rename(archivo, nombreNuevo)
    return(nombreNuevo)


def convert_pdf(nameFile, finalName):  # CONVERT FILE FROM A SELECTED EXT TO PDF
    image = Image.open(nameFile)  # opening image file
    pdf_bytes = img2pdf.convert(image.filename) # converting into chunks using img2pdf
    file = open(finalName + ".pdf", "wb")  # opening or creating pdf file
    file.write(pdf_bytes)  # writing pdf files with chunks
    image.close()  # closing image file
    file.close()  # closing pdf file
    print("Successfully made pdf file: " + file.name)  # output


def compress_file(imageName, newExt):  # COMPRESS FILES IN A ZIP FILE
    zipName = basename(imageName) + '.zip' #Name of the original file
    fileszip = zipfile.ZipFile(pathFile + zipName, 'w')

    for file in os.listdir(pathFile):
        if file.endswith(newExt):
            fileszip.write(file, compress_type=zipfile.ZIP_DEFLATED)
            os.unlink(file)  # Erase the file using shutil module
    fileszip.close()


def main():
    clear()
    imageName = openFile() # Name of the file to split
    fileList = convert_image(imageName, pathFile, ext)

    os.chdir(pathFile)  # Go to the Directory
    for i in range(0, len(fileList)):
        allTextfromImage = ocr_core(fileList[i])  # All text
        subText = read_image(allTextfromImage)  # Only text with need
        #print('\nEsta es la cadena substraída de la imagen:\n' + subText + '\n')
        imageFile = rename_file(fileList[i], subText) # Rename image file with text
        convert_pdf(imageFile, subText)  # convert to PDF again
        os.unlink(imageFile)  # Erase the images files using shutil module

    print('\nTotal de archivo renombrados y comprimidos: ' + str(len(fileList)))
    #MessageBox.showinfo('Total de archivo renombrados y comprimidos:', str(len(fileList)) )
    compress_file(imageName, 'pdf')  # compress all pdf files
    
    
if __name__ == '__main__':
    main()
