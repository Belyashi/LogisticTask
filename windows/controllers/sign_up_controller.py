from PyQt4 import QtCore, QtGui, uic
from windows.widgets import SIGN_UP_WIDGET


class SignUpWidget(QtGui.QWidget):

    _path = SIGN_UP_WIDGET

    def __init__(self):
        super(SignUpWidget, self).__init__()
        uic.loadUi(self._path)

        self.show()


