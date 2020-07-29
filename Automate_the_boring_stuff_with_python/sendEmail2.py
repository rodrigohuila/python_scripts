#! /usr/bin/python3
import os, email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Capturing some info from user
subjectEmail = "An email with attachment from Python"
fromAddr = "rodrigo.huila@gmail.com"
toAddr = "rodrigo.huila@gmail.com" #input(\nWrite the recipient email (PARA)')
password = input("\nWrite the password or passcode (CONTRASEÑA):\n")

#Create a multipart message and set headers
message = MIMEMultipart("alternative")
message["From"] = fromAddr
message["To"] = toAddr
message["subject"] = subjectEmail

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Buen día,<br><br><br> 
       Cordial saludo,<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.<br><br><br>
       Rodrigo Huila<br>
       Planificador
    </p>
            <br>
            <div style="border: 1px solid rgba(37, 201, 255,.5); display: inline-block; border-radius: 3px;">
            <table style="font-family: arial; height:90px; border-collapse: collapse; border: ">
            <tr>
            <td style="padding: 7px">
            <img src="https://www.google.com/s2/u/0/photos/public/AIbEiAIAAABECOaXmNbolOq56AEiC3ZjYXJkX3Bob3RvKig5MTEzMGE0M2ZhMTY2ZDg3ZjE2NmEzOWFmZjIwNGQwOWIxYjYzYjg2MAHDS1i3U-Un2c5uh0eEds7YWkFPFw" 
                alt="" 
                width="80" 
                height="80" 
                style="display:block; border-radius: 50%; margin-right: 7px; float: left"
            >
            <div style="width: 5px; height: 80px; background:#75c8fd; float: right">
            </td>
            <td style="vertical-align:top; padding:7px 14px 7px 3px">
            <strong style="margin: 0; font-size:17px; color: rgba(40, 45, 49,.9); line-height: 24px;      height: 24px; display:block">Hector Rodrigo Huila</strong>
            <p style='font-size:12px; margin: 0px 0 6px; height: 30px'>
                <span style="margin: 0; color: #666">Ingeniero Informático
            </span>
                <br>
                <a href='https://ed.team' style="color: #0B2161;       font-weight: bold">rodrigo.huila@gmail.com</a>
    </p>
            <div id="sociales" ></div>
            </td>
        </tr>
        </table>
    </body>
</html>
"""

#Turn these into plain/html MIMEText object
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

#Attachment
#Directorio donde esta el archivo de excel
os.chdir("/home/rodrigo/Downloads/Victoria")
filename = "DIPLOMAS CALI 18-07-2020 1.pdf"

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
message.attach(part)
text = message.as_string()

# Log and Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(toAddr, password)
    sendmailStatus = server.sendmail(
        toAddr, fromAddr, message.as_string()
    )

if sendmailStatus != {}:
    print('There was a problem sending email to %s: %s' %
          (toAddr, sendmailStatus))
else:
    print('\nThe email to %s was sent correctly' % (toAddr))

#Disconnecting from the SMTP Server
#conn.quit()
