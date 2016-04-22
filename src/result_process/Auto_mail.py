# -*- coding: cp936 -*-
'''
Automatically email test results

'''

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.MIMEBase import MIMEBase
import smtplib
from email import Encoders
import time

def automail_result(result_tardir,testresultname,testresultfilename):
    msg = MIMEMultipart()
    text='''
Hi!
   Attachment is the test results of %s, sent automatically by the IDAT.
Please check it.





------- You are receiving this mail because: -------
You are in the mail list of the IDAT .
Do not reply to this message.Because this message is automatically sent by IDAT.
Thanks.

Test Center
''' %testresultname
    part1 = MIMEText(text,'plain')
    msg.attach(part1)
    part=MIMEBase('application','octet-stream')
    part.set_payload(open('%s'%result_tardir, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=%s'%testresultfilename)
    msg.attach(part)

    mailto_list=["peng.li@i-soft.com.cn","243246714@qq.com"]
    msg['from'] = 'peng.li@i-soft.com.cn'
    msg['subject'] = 'IDAT_testresult'

    try:
        server = smtplib.SMTP()
        server.connect('smtp.qq.com')
        server.login('peng.li@i-soft.com.cn','king314159')
        server.sendmail(msg['from'], mailto_list, msg.as_string())
        server.quit()
    except Exception, errormessage:  
        print str(errormessage) 

