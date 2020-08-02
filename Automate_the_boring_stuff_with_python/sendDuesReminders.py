#! /usr/bin/python3
# sendDuesReminders.py - Sends emails based on their status in spreadsheet.

import os, openpyxl, smtplib, sys

#Directorio donde esta el archivo de excel
os.chdir("/home/rodrigo/Documents/curso_python/Automate_the_boring_stuff_with_python/")

# Open the spreadsheet and get the latest dues status.
wb = openpyxl.load_workbook('duesRecords.xlsx')
#sheet = wb.get_sheet_by_name
sheet = wb['Sheet1']

#lastCol = sheet.get_highest_column()
lastCol = sheet.max_column
latestMonth = sheet.cell(row=1, column=lastCol).value

unpaidMembers = {}
# Check each member's payment status
#for r in range(2, sheet.get_highest_row() + 1):
for r in range(2, sheet.max_row + 1):
    payment = sheet.cell(row=r, column=lastCol).value
    if payment != 'paid':
        name = sheet.cell(row=r, column=1).value
        email = sheet.cell(row=r, column=2).value
        unpaidMembers[name] = email

# Log in to email account.
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('rodrigo.huila@gmail.com', sys.argv[1])

# Send out reminder emails.
for name, email in unpaidMembers.items():
    body = 'Subject: %s dues unpaid.\nDear %s,\nRecords show that you have not paid dues for %s. Please make this payment as soon as possible. Thank you!' % (latestMonth, name, latestMonth)
    print('Sending email to %s...' % email)
    sendmailStatus = smtpObj.sendmail('rodrigo.huila@gmail.com', email, body)

    if sendmailStatus != {}:
        print('There was a problem sending email to %s: %s' % (email, sendmailStatus))
smtpObj.quit()
