#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import favicon
import sys

url = str(sys.argv[1])
if 'https' not in url:
    url = 'https://'+url

icons = favicon.get(url)
icon = icons[0]

del_https_url = url.replace('https://', '')
split_url = del_https_url.split('.')
split_url_first = split_url[0]

if split_url_first == 'www':
    name_file = split_url[1]
elif split_url_first == 'web':
    name_file = split_url[1]
else:
    name_file = split_url_first

resp = requests.get(icon.url, stream=True)
with open('/tmp/{}.{}'.format(name_file, icon.format), 'wb') as img:
     img.write(resp.content)

print('/tmp/{}.{}'.format(name_file, icon.format))

#for i in icons:
#    print(i.url)
