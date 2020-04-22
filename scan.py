#!/bin/python2.7
#-*- coding: utf-8 -*-
"""
Copyright (c) 2020 Dst_207
"""

"""
Silahkan dipelajari slur tools nya
tapi asal jangan di recode/reupload ya
kak kalo mau pelajari pelajari aja ok!
"""

import os, time, sys, json, re, requests
from var_animate import *

logo = banner('Subdomain','Dst_207','0.1 Scanner')
alert = animvar()
input = animinput()
## Coloring ##
c = color().show
me = c('red')
bi = c('blue')
i = c('green')
cy = c('cyan')
pu = c('white')
os.system('clear')
print(logo)
print('{}Team{}: {}Black Coder Crush\n').format(cy,me,pu)
host = input.ask('Host')
if 'www' in host:
    host = host.replace('www.','')
elif 'http://' in host:
    host = host.replace('http://','')
elif 'https://' in host:
    host = host.replace('https://','')

r = requests.get('https://api.hackertarget.com/hostsearch/?q='+host).text
if 'error check your search parameter' in r:
   time.sleep(1)
   print('\n'+alert.false('Sepertinya Host Yg anda masukan salah'))
   time.sleep(1)
   exit()

scan = r.split('\n')
a = 1

for i in scan:
    rgx = re.search('(.*?),(.*)',i)
    print('{}   ---- {}{} {}----').format(bi,me,a,bi)
    try:
       print('{}Host{}: {}{}').format(cy,me,pu,rgx.group(1))
       print('{}Ip{}: {}{}').format(cy,me,pu,rgx.group(2))
    except AttributeError: pass
    a += 1
