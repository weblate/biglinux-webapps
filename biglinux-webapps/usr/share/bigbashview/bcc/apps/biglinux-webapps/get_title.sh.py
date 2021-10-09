#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup

url = sys.argv[1].strip()
if 'https' not in url:
    url = 'https://'+url
try:
    r = requests.get(url)
    html_parse = BeautifulSoup(r.content, 'html.parser')
    html_title = html_parse.title.string.strip()
    title = html_title.replace('  ', ' ')
    _title = title.replace('|', '')
    print(_title)
except:
    sys.exit()
