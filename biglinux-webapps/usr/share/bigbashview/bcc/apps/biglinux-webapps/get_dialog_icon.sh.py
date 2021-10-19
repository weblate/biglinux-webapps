#!/usr/bin/env python3

from PySide2.QtWidgets import QFileDialog, QApplication
from PySide2.QtGui import QIcon
import sys, os

app = QApplication(sys.argv)

class Dialog(QFileDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.setWindowIcon(QIcon.fromTheme('insert-image'))
        self.resize(900, 500)
        qtRectangle = self.frameGeometry()
        centerPoint = app.primaryScreen().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        file_name, _ = self.getOpenFileName(self,  self.tr('Open Image'),
                                                   os.path.expanduser('~'),
                                                   self.tr('Images (*.svg *.png *.xpm *.jpg *.jpeg *.ico)'),
                                                   options=self.DontUseNativeDialog)

        if file_name:
            base_name = os.path.basename(file_name)
            name_file, ext = os.path.splitext(base_name)

            if ext in ('.svg', '.ico', '.jpg', '.jpeg', '.xbm', '.webp'):
                os.system('''convert {0} -thumbnail 48x48 \
                                         -alpha on        \
                                         -background none \
                                         -flatten /tmp/{1}.png'''.format(file_name, name_file))
                print('/tmp/%s.png' % name_file)
            else:
                print(file_name)
            sys.exit()
        else:
            sys.exit()

Dialog()
app.exec_()
