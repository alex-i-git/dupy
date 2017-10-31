#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
import conf
import os
from email.mime.text import MIMEText

msg['Subject'] = 'Disk usage'
msg['From'] = me
msg['To'] = you
s = smtplib.SMTP()
fs = '/logs'
st=os.statvfs(fs)
stat = int((st.f_blocks-st.f_bfree)/float(st.f_blocks)*100)
msg = MIMEText(stat)

s.connect()
s.sendmail(me, you, msg.as_string())
s.quit()
