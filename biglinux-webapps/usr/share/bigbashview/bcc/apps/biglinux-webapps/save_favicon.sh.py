#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import sys, os
from urllib.parse import urlparse

def url_parse(url):
    try:
        url_http = url if 'https://' in url else 'https://'+url
        _url = urlparse(url_http)
        _url_split = _url.netloc.split('.')

        if _url_split[1] == 'github': return 'github'

        matches = ['webz', 'webk', 'web', 'www', 'mobile', 'hp', 'static.xx', 'm']
        name = _url_split[0] if not any(x in _url_split[0] for x in matches) else _url_split[1]
        return name
    except:
        return

url = sys.argv[1].strip()
ext = os.path.splitext(url)[1]
name_file = url_parse(url)

try:
    resp = requests.get(url, stream=True)
    with open('/tmp/{}{}'.format(name_file, ext), 'wb') as img:
         img.write(resp.content)

    if ext in ('.svg', '.ico', '.jpg', '.jpeg', '.xbm', '.webp'):
        os.system('''convert /tmp/{0}{1} -thumbnail 32x32 \
                                         -alpha on        \
                                         -background none \
                                         -flatten /tmp/{0}.png'''.format(name_file, ext))
        os.remove('/tmp/{0}{1}'.format(name_file, ext))

    print('/tmp/{}.png'.format(name_file))
except:
    sys.exit()
