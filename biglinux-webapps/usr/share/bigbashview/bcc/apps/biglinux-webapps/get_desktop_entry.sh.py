#!/usr/bin/env python3

from xdg import DesktopEntry, BaseDirectory
import glob, json

HOME = BaseDirectory.xdg_data_home
files = glob.glob(HOME+'/applications/*custom.desktop')

for f in files:
    filedesk = DesktopEntry.DesktopEntry(f)
    fileexec = filedesk.getExec()

    if not fileexec.startswith('/home'):
        _execfile = fileexec.split()[3].replace('--app=', '')
    else:
        with open(fileexec, 'r') as fx:
            line = fx.readlines()[39]
            _execfile = line.split()[8].replace('"', '')

    x = { "Name" : filedesk.getName(), "Exec" : _execfile, "Icon" : filedesk.getIcon()}
    print(json.dumps(x))
