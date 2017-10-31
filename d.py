#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
#импорт почтовых адресов из cnf.py
import cnf
import os
from email.mime.text import MIMEText

s = smtplib.SMTP()
fs = '/logs'
st=os.statvfs(fs)
stat = str(int((st.f_blocks-st.f_bfree)/float(st.f_blocks)*100)) + '%'
msg = MIMEText(stat)
msg['Subject'] = 'sadm disk usage'
msg['From'] = cnf.me
msg['To'] = cnf.you


s.connect()
s.sendmail(cnf.me, cnf.you, msg.as_string())
s.quit()