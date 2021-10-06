#/usr/bin/env python3
from PySide2.QtWidgets import QFileDialog, QApplication
import sys


class Dialog(QFileDialog):
    def __init__(self):
        super().__init__()

        fname = self.getOpenFileName(None, 'Open file', '/home')
        if fname:
            print(fname[0])
        sys.exit()

app = QApplication(sys.argv)
Dialog()
app.exec_()
