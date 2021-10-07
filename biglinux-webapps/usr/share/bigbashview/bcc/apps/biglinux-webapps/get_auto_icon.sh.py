#!/usr/bin/env python3

import gi, sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from urllib.parse import urlparse

def url_parse(url):
    _url = urlparse(url)

    print(_url.netloc.split('.')[1])

def get_icon(icon_name):
    icon_theme = Gtk.IconTheme.get_default()
    icon_info = icon_theme.lookup_icon(icon_name, 48, 0)
    try:
        filename = icon_info.get_filename()
        print(filename)
    except:
        sys.exit()

if __name__ == "__main__":
    url_parse(sys.argv[1])
