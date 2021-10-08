#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import favicon
import sys
#import subprocess

url = sys.argv[1].strip()

#url = subprocess.getoutput('zenity --entry --text=$"Insira a URL:" --width=400 --title=$"BigLinux WebApps"')

if 'https' not in url:
    url = 'https://'+url

icons = favicon.get(url)
if len(icons) > 1:
    for i in icons:
         print(i.url)
else:
    print(icons[0].url)
