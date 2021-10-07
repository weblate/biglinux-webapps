#!/usr/bin/env python3

import gi, sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from urllib.parse import urlparse

def url_parse(url):
    url_http = url if url in 'https://' else 'https://'+url
    _url = urlparse(url_http)
    return _url
    _url_split = _url.netloc.split('.')[0]
    name = _url_split if _url_split not in ('webz', 'webk', 'web', 'www') else _url.netloc.split('.')[1]
    return name

def get_icon(icon_name):
    icon_theme = Gtk.IconTheme.get_default()
    icon_info = icon_theme.lookup_icon(icon_name, 48, 0)
    try:
        filename = icon_info.get_filename()
        print(filename)
        sys.exit()
    except:
        sys.exit()

if __name__ == "__main__":
    #get_icon(url_parse(sys.argv[1]))
    print(url_parse(sys.argv[1]))
