#!/usr/bin/env python3

import sys
import os
import glob
import favicon
from urllib.parse import urlparse


def url_parse(url):
    url_http = url if 'https://' in url else 'https://'+url
    _url = urlparse(url_http)
    try:
        if _url.netloc.split('.')[1] == 'github': return 'github'

        _url_split = _url.netloc.split('.')[0]
        matches = ['webz', 'webk', 'web', 'www']
        name = _url_split if not any(x in _url_split for x in matches) else _url.netloc.split('.')[1]
        return name
    except:
        return


def get_img_local(img_name):

    images_all = []

    images_home = glob.glob(os.path.expanduser('~')+'/*/*.*', recursive=True)
    images_home_share = glob.glob(os.path.expanduser('~')+'/.local/share/icons/**/*.*', recursive=True)
    images_system_share = glob.glob('/usr/share/icons/**/*.*', recursive=True)
    images_system_pix = glob.glob('/usr/share/pixmaps/*.*', recursive=True)

    ext = ['.png', '.jpg', '.jpeg', '.svg', '.xpm']
    images_all.extend(i for i in images_home
                      if img_name in i.lower()
                      and os.path.splitext(i)[1] in ext)

    images_all.extend(s for s in images_home_share
                      if img_name in s.lower()
                      and os.path.splitext(s)[1] in ext)

    images_all.extend(z for z in images_system_pix
                      if img_name in z.lower()
                      and os.path.splitext(z)[1] in ext)

    images_all.extend(x for x in images_system_share
                      if img_name in x.lower()
                      and os.path.splitext(x)[1] in ext)

    for img in images_all:
        if img.endswith('.svg'):
            with open(img, 'r') as f:
                print(f.name)
                print(f.read())

        else:
            print(img)


def get_favicon_site(url):

    if 'https' not in url:
        url = 'https://'+url
    try:
        icons = favicon.get(url)
        if len(icons) > 1:
            for i in icons:
                 print(i.url)
        else:
            print(icons[0].url)
    except:
        return


if __name__ == "__main__":
    #get_icon(url_parse(sys.argv[1]))
    arg = sys.argv[1].strip()
    get_favicon_site(arg)
    get_img_local(url_parse(arg))
    #print(url_parse(sys.argv[1]))