#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import favicon
import subprocess

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
            html = subprocess.getoutput('./save_favicon.sh.py %s' % url_icon)

        print(html)
    except:
        return

if __name__ == "__main__":
    url = sys.argv[1].strip()
    get_favicon_site(url)
