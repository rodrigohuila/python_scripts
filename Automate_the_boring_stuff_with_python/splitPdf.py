#! /usr/bin/python3

import os
import PyPDF2

path = '/home/rodrigo/Downloads/'
contentAll = ''

print('\nDigite el nombre del Documento:')
pdfName = input()

# Open the pdf file
pdfFileObj = open( path + pdfName, 'rb')
# Read info
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
print ('\nEl documento tiene: ' + str(pdfReader.numPages) + ' páginas')

# Read the content of the first page
pageObj = pdfReader.getPage(0)
content = pageObj.extractText()
print ('\nEl contenido de la primera página del PDF es el siguiente: \n' + content)

# Read the content of all pages
for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    contentAll = contentAll + pageObj.extractText()
    
print ('\nEl contenido de todos los PDF es: \n' + contentAll)


#Split a document
def pdf_splitter(pathpdfName):
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter = PyPDF2.PdfFileWriter()
        pdfWriter.addPage(pageObj)
        output_filename = 'page_{}_{}'.format(
            pageNum+1, pdfName)
        os.chdir('/home/rodrigo/Downloads/Victoria')
        with open(output_filename, 'wb') as out:
            pdfWriter.write(out)
        print('Created: {}'.format(output_filename))

if __name__ == '__main__':
    pdf_splitter(path + pdfName)    
    