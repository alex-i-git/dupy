#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
import cnf
import os
from email.mime.text import MIMEText

s = smtplib.SMTP()
fs = '/logs'
st=os.statvfs(fs)
stat = str(int((st.f_blocks-st.f_bfree)/float(st.f_blocks)*100))
msg = MIMEText(stat)
msg['Subject'] = 'disk usage'
msg['From'] = me
msg['To'] = you


s.connect()
s.sendmail(me, you, msg.as_string())
s.quit()