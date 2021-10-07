#!/usr/bin/env python3

from PySide2.QtWidgets import QFileDialog, QApplication, QWidget
from PySide2.QtGui import QIcon
import sys, os

app = QApplication(sys.argv)

class Dialog(QWidget):
    def __init__(self):

        super(Dialog, self).__init__()

        self.setWindowIcon(QIcon.fromTheme('insert-image'))
        self.resize(900, 500)
        qtRectangle = self.frameGeometry()
        centerPoint = app.primaryScreen().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        file_name, _ = QFileDialog.getOpenFileName(self,
                                                   self.tr('Open Image'),
                                                   os.path.expanduser('~'),
                                                   self.tr('Images (*.svg *.png *.xpm *.jpg *.jpeg *.ico)'),
                                                   options=QFileDialog.DontUseNativeDialog)
        if file_name:
            print(file_name)
            sys.exit()
        else:
            sys.exit()


if __name__ == "__main__":
    Dialog()
    app.exec_()
