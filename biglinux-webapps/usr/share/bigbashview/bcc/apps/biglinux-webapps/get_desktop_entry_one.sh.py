#!/usr/bin/env python3

from xdg import DesktopEntry
from os import environ
from sys import argv, exit

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

    environ.copy()
    environ["NAME"] = filedesk.getName()
    environ["URL"] = _urlfile
    environ["ICON"] = filedesk.getIcon()
    environ["FILEDESK"] = f
    environ.update()
    exit()

filedesk = argv[1]
update_env(filedesk)
