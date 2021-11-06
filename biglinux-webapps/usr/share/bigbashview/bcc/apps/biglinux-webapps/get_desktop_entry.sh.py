#!/usr/bin/env python3

from xdg import DesktopEntry, BaseDirectory
import glob, json

HOME = BaseDirectory.xdg_data_home
files = glob.glob(HOME+'/applications/*custom.desktop')

dict = {
        "NAME" : [],
        "URL" : [],
        "ICON" : []
       }

for f in files:
    filedesk = DesktopEntry.DesktopEntry(f)
    fileexec = filedesk.getExec()
    fileexec_chrom = fileexec.split()[3].replace('--app=', '')

    if not fileexec.startswith('/home'):
        _urlfile = (fileexec_chrom
                if fileexec_chrom != '--profile-directory=Default'
                else fileexec.split()[4].replace('--app=', ''))
    else:
        with open(fileexec, 'r') as fx:
            line = fx.readlines()[39]
            _urlfile = line.split()[8].replace('"', '')

    dict["NAME"].append(filedesk.getName())
    dict["URL"].append(_urlfile)
    dict["ICON"].append(filedesk.getIcon())

print(json.dumps(dict, ensure_ascii=False))
