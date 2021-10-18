#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import favicon
import requests
import random

def get_favicon_site(url):
    try:
        if 'https' not in url:
            url = 'https://'+url

        icons = favicon.get(url)
        html = ''
        if len(icons) > 1:
            for i in icons:
                 html += '''
                 <div class="col-3 text-center" id="input_img">
                    <img class="img-thumbnail" src="%s"/><br>
                    <span class="spinner-border spinner-border-sm mt-2 text-primary"
                          role="status" aria-hidden="true" id="btn-spin"></span>
                 </div>''' % i.url
        else:
            url_icon = icons[0].url
            base_name = os.path.basename(url_icon)
            name_file, ext = os.path.splitext(base_name)
            if name_file == 'favicon':
                name_file = '%s-%s' % (name_file, random.randint(0, 10000000))

            resp = requests.get(url_icon, stream=True)
            with open('/tmp/{}{}'.format(name_file, ext), 'wb') as img:
                 img.write(resp.content)

            if ext in ['.svg', '.ico', '.jpg', '.jpeg', '.xbm', '.webp']:
                os.system('''convert /tmp/{0}{1} -thumbnail 32x32 \
                                                 -alpha on        \
                                                 -background none \
                                                 -flatten /tmp/{0}.png'''.format(name_file, ext))
                os.remove('/tmp/{0}{1}'.format(name_file, ext))
                html = '/tmp/{}.png'.format(name_file)
            else:
                html = '/tmp/{}.png'.format(name_file)

        print(html)
    except:
        return

if __name__ == "__main__":
    url = sys.argv[1].strip()
    html_full = get_favicon_site(url)
