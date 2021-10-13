#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import sys, os
from urllib.parse import urlparse

def url_parse(url_http):
    _url = urlparse(url_http)
    _url_split = _url.netloc.split('.')[0]
    matches = ['webz', 'webk', 'web', 'www', 'mobile', 'hp', 'static.xx', 'm']
    name = _url_split if not any(x in _url_split for x in matches) else _url.netloc.split('.')[1]
    return name

url = sys.argv[1].strip()
ext = os.path.splitext(url)[1]
url_http = url if 'https://' in url else 'https://'+url
name_file = url_parse(url_http)

try:
    resp = requests.get(url, stream=True)
    with open('/tmp/{}{}'.format(name_file, ext), 'wb') as img:
         img.write(resp.content)

    if ext in ('.svg', '.ico', '.jpg', '.jpeg', '.xbm', '.webp'):
        os.system('''convert /tmp/{0}{1} -thumbnail 32x32 \
                                         -alpha on        \
                                         -background none \
                                         -flatten /tmp/{0}.png'''.format(name_file, ext))
        ext = '.png'

    print('/tmp/{}{}'.format(name_file, ext))
except:
    sys.exit()