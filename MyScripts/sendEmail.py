import os, smtplib, sys


conn = smtplib.SMTP('smtp.gmail.com', 587)
#type(conn)
#conn
conn.ehlo()
conn.starttls()

#Capturing info from user       
#print('\nWrite your email (DE):')
fromAddr = 'rodrigo.huila@gmail.com' #str(input())
#password = str(input('\nWrite the password or passcode (CONTRASEÑA):\n'))
toAddr = str(input('\nWrite the recipient email (PARA)\n'))

#Login
conn.login(fromAddr, sys.argv[1])

#Capturing subject and body of the email
subjectEmail = str(input('\nWrite the Subjet of the email (ASUNTO):\n'))
bodyEmail = str(input('\nWrite the body of the email (CUERPO DEL MENSAJE):\n'))  

#Send the email
sendmailStatus = conn.sendmail(fromAddr, toAddr, ('Subject: ' + subjectEmail + '\n' + bodyEmail))

#Verification
if sendmailStatus != {}:
    print('There was a problem sending email to %s: %s' % (toAddr, sendmailStatus))
else:
    print('\nThe email to %s was sent correctly' % (toAddr))
#Disconnecting from the SMTP Server
conn.quit()
