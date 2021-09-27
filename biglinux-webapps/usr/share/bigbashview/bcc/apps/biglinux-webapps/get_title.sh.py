#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup

url = str(sys.argv[1])
if 'https' not in url:
    url = 'https://'+url
r = requests.get(url)
html_parse = BeautifulSoup(r.content, 'html.parser')
html_title = html_parse.title.string.strip()
title = html_title.replace('  ', ' ')
print(title)
