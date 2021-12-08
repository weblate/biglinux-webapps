#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import favicon
import subprocess

def get_favicon_site(url):
    try:
        icons = favicon.get(url)
        html = ''
        num=1
        if len(icons) > 1:
            for i in icons:
                html += '''
                <div class="col text-center mb-3" id="input_img">
                    <img class="img-thumbnail d-block mx-auto" src="%s"/>
                    <cite style="font-size:9pt">%s- %s</cite><br/>
                    <span class="spinner-border spinner-border-sm mt-2 text-primary"
                      role="status" aria-hidden="true" id="btn-spin"></span>
                </div>''' % (i.url, num, os.path.basename(i.url))
                num+=1
        else:
            url_icon = icons[0].url
            html = subprocess.getoutput('./save_favicon.sh.py %s' % url_icon)

        print(html, end='')
    except:
        return

url = sys.argv[1].strip()
if 'https' not in url:
    url = 'https://'+url
get_favicon_site(url)
