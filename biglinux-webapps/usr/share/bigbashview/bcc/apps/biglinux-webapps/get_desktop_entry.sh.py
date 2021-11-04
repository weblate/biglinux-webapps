#!/usr/bin/env python3

from xdg.DesktopEntry import DesktopEntry
from xdg import BaseDirectory
import glob

HOME = BaseDirectory.xdg_data_home
DIR = glob.glob(HOME+'/applications/*custom.desktop')

for f in DIR:
    FileEntry = DesktopEntry(f)
    print(FileEntry.getName(), end='\n\n')
    print(FileEntry.getIcon(), end='\n\n')
    print(FileEntry.getExec(), end='\n\n\n\n')