#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import requests
import re
from bs4 import BeautifulSoup

def get_title(url):
    try:
        r = requests.get(url)
        if r.status_code >= 400: return
        html_parse = BeautifulSoup(r.content, 'html.parser')
        html_title = html_parse.title.string.strip()
        title = re.sub(r'[^\w]',' ', html_title)
        _title = re.sub(r'\s+',' ', title)
        print(_title)
    except:
        sys.exit()

if __name__ == "__main__":
    url = sys.argv[1].strip()
    if 'https' not in url:
        url = 'https://'+url
    get_title(url)
