#!/usr/bin/env python3

from PySide2.QtWidgets import QFileDialog, QApplication
from PySide2.QtGui import QIcon
import sys


class Dialog(QFileDialog):
    def __init__(self):
        super(Dialog, self).__init__()

        self.setWindowIcon(QIcon.fromTheme('insert-image'))

        fname = self.getOpenFileName(None, 'Images', QIcon.themeSearchPaths()[2], 'Images (*.png *.xpm *.jpg)')
        file_name = fname[0]
        if file_name:
            print(file_name)
            sys.exit()
        else:
            sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog()
    app.exec_()
