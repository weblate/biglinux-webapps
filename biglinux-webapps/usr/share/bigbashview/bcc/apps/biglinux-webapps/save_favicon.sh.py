#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import sys
import os
from random import randint
from io import BytesIO
from PIL import Image, UnidentifiedImageError

def save(url):
    base_name = os.path.basename(url)
    string, extension = os.path.splitext(base_name)
    name_file = ''.join(c for c in string if c.isalnum())

    if extension:
        ext = extension
    else:
        ext = '.png'

    if name_file == 'favicon':
        name_file = '%s-%s' % (name_file, randint(0, 10000000))

    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
        'AppleWebKit/537.36 (KHTML, like Gecko)'
        'Chrome/50.0.2661.102 Safari/537.36'
        }
        resp = requests.get(url, stream=True, headers=headers)
        with Image.open(BytesIO(resp.content)) as img:
            if img.verify:
                img.save('/tmp/{}{}'.format(name_file, ext))

                if img.format != 'PNG':
                    status = os.system('''convert /tmp/{0}{1} -resize 32x32^ \
                                                     -alpha on        \
                                                     -background none \
                                                     -flatten /tmp/{0}.png'''.format(name_file, ext))
                    os.remove('/tmp/{}{}'.format(name_file, ext))
                    print('/tmp/%s.png' % name_file, end='')
                else:
                    print('/tmp/%s.png' % name_file, end='')

    except UnidentifiedImageError:
        status = os.system('''wget -q {0} -O /tmp/{1}{2}
                     convert /tmp/{1}{2} -thumbnail 32x32^ \
                                         -alpha on        \
                                         -background none \
                                         -flatten /tmp/{1}.png'''.format(url, name_file, ext))
        os.remove('/tmp/{}{}'.format(name_file, ext))
        print('/tmp/%s.png' % name_file, end='')

    else:
        return

url = sys.argv[1].strip()
save(url)
