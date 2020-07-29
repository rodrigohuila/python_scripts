#! /usr/bin/python3

import smtplib, sys, os, openpyxl, email

from email import encoders
from string import Template
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'rodrigo.huila@gmail.com'
PASSWORD = (sys.argv[1])
PATH = '/home/rodrigo/Desktop/emailsPython'
# Path were is the files
os.chdir(PATH)
ext = '.pdf'
contacts = 'contacts.xlsx'
msgTemplate = 'message.txt'

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    names = []
    emails = []
    wb = openpyxl.load_workbook(filename)
    sheet = wb['Sheet1']
    
    for r in range(2, sheet.max_row + 1):
          name=(sheet.cell(row=r, column=1).value)
          names.append(name)
          email=(sheet.cell(row=r, column=2).value)
          emails.append(email)
    return names, emails


def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def search_files(names):
    """
    Return a list of names of files to attach to the msg
    """
    files = []
    
    for i in range (0, len(names)):
        check = False    
        for filename in os.listdir(PATH):
            name = names[i].lower()
            name = name[0:10]
            if filename.endswith(ext):
                fileNewName = str(filename)
                fileNewName = fileNewName.replace('_', ' ')
                fileNewName = fileNewName.lower()
                if fileNewName.find(name) >=0:
                    files.append(filename)
                    check = True
                elif name.find(fileNewName) >=0:
                    files.append(filename)
                    check = True
        if check == False:
            files.append(None)  
    return(files)    
        


def main():
    names, emails = get_contacts(contacts)  # read contacts
    message_template = read_template(msgTemplate)
    attach = search_files(names)

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    i = 0

    # FOR EACH CONTACT, SEND THE EMAIL:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message
            
        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "This is TEST"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        #ATTACH FILES TO THE EMAIL
        #Directorio donde esta el archivo a adjuntar
        
        #search_files(names) #'test.pdf'
        filename = attach[i]
        if filename != None:
            # Open PDF file in binary mode
            with open(filename, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)
            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )
            # Add attachment to message and convert message to string
            msg.attach(part)
            #text = message.as_string()
            # SEND THE MESSAGE WITH ATTACHED.
            s.send_message(msg)
            del msg
            i = (i + 1)
        else: 
            # SEND THE MESSAGE WITHOUT ATTACHED.
            s.send_message(msg)
            del msg
            i = (i + 1)

    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == '__main__':
    main()
