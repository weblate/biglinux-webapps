#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import glob
import favicon
import requests
from urllib.parse import urlparse


def url_parse(url):
    try:
        url_http = url if 'https://' in url else 'https://'+url
        _url = urlparse(url_http)

        if _url.netloc.split('.')[1] == 'github': return 'github'

        _url_split = _url.netloc.split('.')
        matches = ['webz', 'webk', 'web', 'www', 'mobile', 'hp', 'static.xx', 'm']
        name = _url_split[0] if not any(x in _url_split[0] for x in matches) else _url_split[1]
        return name
    except:
        return


def get_img_local(img_name):
    try:
        images_all = []
        HOME = os.path.expanduser('~')
        HOME_USER = HOME+'/*'
        HOME_SHARE = HOME+'/.local/share/icons/**'
        SHARE = '/usr/share'
        SHARE_ICONS = SHARE+'/icons/**'
        SHARE_PIX = SHARE+'/pixmaps'

        images_home = glob.glob(HOME_USER+'/*%s*.*' % img_name, recursive=True)
        images_home_share = glob.glob(HOME_SHARE+'/*%s*.*' % img_name, recursive=True)
        images_system_share = glob.glob(SHARE_ICONS+'/*%s*.*' % img_name, recursive=True)
        images_system_pix = glob.glob(SHARE_PIX+'/*%s*.*' % img_name, recursive=True)
        ext = ['.png', '.jpg', '.jpeg', '.svg', '.xpm']

        images_all.extend(i for i in images_home
                          if os.path.splitext(i)[1] in ext)

        images_all.extend(s for s in images_home_share
                          if os.path.splitext(s)[1] in ext)

        images_all.extend(z for z in images_system_pix
                          if os.path.splitext(z)[1] in ext)

        images_all.extend(x for x in images_system_share
                          if os.path.splitext(x)[1] in ext)

        html = ''
        for img in images_all:
            if img.endswith('.svg'):
                with open(img, 'r') as f:
                    html += '<div class="col-3 img-thumbnail text-center">%s</div>' % f.read()
            else:
                html += '<div class="col-3"><img class="img-thumbnail" src="%s"/></div>' % img
        return html
    except:
        return


def get_favicon_site(url, name_file):
    try:
        if 'https' not in url:
            url = 'https://'+url

        icons = favicon.get(url)
        html = ''
        if len(icons) > 1:
            for i in icons:
                 html += '''
                 <div class="col-3">
                    <img class="img-thumbnail" src="{0}" id="input_img"/>
                 </div>'''.format(i.url)
        else:
            ext = os.path.splitext(icons[0].url)[1]
            resp = requests.get(icons[0].url, stream=True)
            with open('/tmp/{}{}'.format(name_file, ext), 'wb') as img:
                 img.write(resp.content)

            if ext in ('.svg', '.ico', '.jpg', '.jpeg', '.xbm', '.webp'):
                os.system('''convert /tmp/{0}{1} -thumbnail 32x32 \
                                                 -alpha on        \
                                                 -background none \
                                                 -flatten /tmp/{0}.png'''.format(name_file, ext))
                os.remove('/tmp/{0}{1}'.format(name_file, ext))

            html = '/tmp/{}.png'.format(name_file)
        return html
    except:
        return


if __name__ == "__main__":
    arg = sys.argv[1].strip()

    try:
        html_full = get_favicon_site(arg, url_parse(arg))
        print(html_full)
    except:
        html_full = get_img_local(url_parse(arg))
        print(html_full)
