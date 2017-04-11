#!/usr/bin/env python
# -*- encode: utf-8 -*-
__author__='Siwei Chen <chensiwei1990@gmail.com>'

import telnetlib
import time

USERNAME = b'TODO_YOUR_USERNAME'
PASSWORD = b'TODO_YOUR_PASSWORD'

# 开始连接
print('Start Connecting...')
tn = telnetlib.Telnet(host='pop3.newsmth.net', port=110)
time.sleep(5)
print(tn.read_until(b'\r\n').decode(encoding='ascii'))

# 已成功连接
# 输入用户名
print('Successfully Connected')
print('Checking username...')
tn.write(b'user '+USERNAME+b'\n')
print(tn.read_until(b'\r\n').decode(encoding='ascii'))

# 输入密码
print('Verifying password...')
tn.write(b'pass '+PASSWORD+b'\n')
num = int(tn.read_until(b'\r\n').decode(encoding='ascii').split(' ')[3])

print('\n%d mails in total.' % num)

with open(USERNAME.decode(encoding='ascii')+'.txt','w') as f:
    for i in range(1,num+1):
        print('Downlowding mail(s) %d/%d' %(i,num))
        cmd = b'retr '+bytes(str(i),'ascii')+b'\n'
        #print(cmd)
        tn.write(cmd)
        time.sleep(1)
        ret = tn.read_very_eager()
        #print(ret)
        f.write(ret.decode(encoding='gbk'))

print('\nDownloading Completed.')
tn.close()
