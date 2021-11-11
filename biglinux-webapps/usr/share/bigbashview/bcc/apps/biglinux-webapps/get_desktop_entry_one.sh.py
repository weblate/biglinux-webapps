#!/usr/bin/env python3

from xdg import DesktopEntry
import json
from sys import argv

def update_env(f):
    filedesk = DesktopEntry.DesktopEntry(f)
    fileexec = filedesk.getExec()
    if not fileexec.startswith('/home'):
        fileexec_chrom = fileexec.split()[3].replace('--app=', '')
        _urlfile = (fileexec_chrom
                if fileexec_chrom != '--profile-directory=Default'
                else fileexec.split()[4].replace('--app=', ''))
    else:
        with open(fileexec, 'r') as fx:
            line = fx.readlines()[39]
            _urlfile = line.split()[8].replace('"', '')

    dict = {}
    dict['NAME'] = filedesk.getName()
    dict['URL'] = _urlfile
    dict['ICON'] = filedesk.getIcon()
    dict['FILE'] = f
    print(json.dumps(dict))

filedesk = argv[1]
update_env(filedesk)
