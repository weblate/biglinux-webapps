#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import sys
import os
import random

def save(url_icon):
    base_name = os.path.basename(url_icon)
    base_name_split = os.path.splitext(base_name)
    if base_name_split[0] == 'favicon':
        name_file = '%s-%s' % (base_name_split[0], random.randint(0, 10000000))
    else:
        name_file = base_name_split[0]
    ext = base_name_split[1]

    try:
        resp = requests.get(url, stream=True)
        with open('/tmp/{}{}'.format(name_file, ext), 'wb') as img:
             img.write(resp.content)

        if ext in ['.svg', '.ico', '.jpg', '.jpeg', '.xbm', '.webp']:
            os.system('''convert /tmp/{0}{1} -thumbnail 32x32 \
                                             -alpha on        \
                                             -background none \
                                             -flatten /tmp/{0}.png'''.format(name_file, ext))
            os.remove('/tmp/{0}{1}'.format(name_file, ext))
            print('/tmp/{}.png'.format(name_file))
        else:
            print('/tmp/{}.png'.format(name_file))
    except:
        return

if __name__ == "__main__":
    url = sys.argv[1].strip()
    save(url)
