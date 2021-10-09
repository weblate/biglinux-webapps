#!/usr/bin/env python3

import gi, sys, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
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

def get_icon(icon_name):
    try:
        icon_theme = Gtk.IconTheme.get_default()
        icon_info = icon_theme.lookup_icon(icon_name, 128, 0)
        filename = icon_info.get_filename()
        ext = os.path.splitext(filename)[1]
        name_file = os.path.basename(filename).split('.')[0]
        if ext in ('.svg', '.ico', '.jpg', '.jpeg', '.xbm', '.webp'):
            os.system('''convert {0} -thumbnail 32x32 \
                                     -alpha on        \
                                     -background none \
                                     -flatten /tmp/{1}.png'''.format(filename, name_file))
            print('/tmp/%s.png' % name_file)
        else:
            print(filename)
        sys.exit()
    except:
        sys.exit()

if __name__ == "__main__":
    get_icon(url_parse(sys.argv[1]))
    #print(url_parse(sys.argv[1]))
