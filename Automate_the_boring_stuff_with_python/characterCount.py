# Dictionaries

#este modulo organiza la impresión
import pprint
#copy a paste 
import pyperclip
import time
 
# ''' => allow me to scape everything inside
# message = '''The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

# This eBook is for the use of anyone anywhere at no cost and with
# almost no restrictions whatsoever.  You may copy it, give it away or
# re-use it under the terms of the Project Gutenberg License included
# with this eBook or online at www.gutenberg.org/license

# This Web site includes information about Project Gutenberg-tm,
# including how to make donations to the Project Gutenberg Literary
# Archive Foundation, how to help produce our new eBooks, and how to
# subscribe to our email newsletter to hear about new eBooks.'''

print('Copy the characters that you wanna count: (ctr + c)')
time.sleep(5) # Delays for 5 seconds
message = pyperclip.paste()
count = {}

# Create a dictionary where key=letter and value=how many times the letter apears in the message
for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

#imprime directamente en pantalla
#pprint.pprint(count)

#Guarda en una varaible y luego imprime
rjtext = pprint.pformat(count)
print(rjtext)