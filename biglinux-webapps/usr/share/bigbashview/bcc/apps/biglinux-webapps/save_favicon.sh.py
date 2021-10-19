#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import sys
import os
import random
import io
from PIL import Image, UnidentifiedImageError

def save(url):
    base_name = os.path.basename(url)
    name_file, ext = os.path.splitext(base_name)
    if name_file == 'favicon':
        name_file = '%s-%s' % (name_file, random.randint(0, 10000000))

    try:
        resp = requests.get(url, stream=True, timeout=3)
        with Image.open(io.BytesIO(resp.content)) as img:
            img.save('/tmp/{}{}'.format(name_file, ext))

            if img.verify:
                if img.format != 'PNG':
                    os.system('''convert /tmp/{0}{1} -thumbnail 32x32 \
                                                     -alpha on        \
                                                     -background none \
                                                     -flatten /tmp/{0}.png'''.format(name_file, ext))
                    os.remove('/tmp/{}{}'.format(name_file, ext))
                    print('/tmp/%s.png' % name_file)
                else:
                    print('/tmp/%s.png' % name_file)

    except UnidentifiedImageError:
        os.system('''wget -q {0} -O /tmp/{1}{2}
                     convert /tmp/{1}{2} -thumbnail 32x32 \
                                         -alpha on        \
                                         -background none \
                                         -flatten /tmp/{1}.png'''.format(url, name_file, ext))
        os.remove('/tmp/{}{}'.format(name_file, ext))
        print('/tmp/%s.png' % name_file)

    else:
        return

url = sys.argv[1].strip()
save(url)
