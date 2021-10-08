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
            ext = os.path.splitext(file_name)[1]
            name_file = os.path.basename(file_name).split('.')[0]
            if ext in ('.svg', '.ico', '.jpg', '.jpeg', '.xbm', '.webp'):
                os.system('''convert {0} -thumbnail 32x32 \
                                         -alpha on        \
                                         -background none \
                                         -flatten /tmp/{1}.png'''.format(filename, name_file))
                print('/tmp/%s.png' % name_file)
            else:
                print(file_name)
            sys.exit()
        else:
            sys.exit()

Dialog()
app.exec_()
