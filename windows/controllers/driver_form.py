from PyQt4 import QtGui, QtCore, uic
from windows.widgets import DRIVERS_FORM


class DriverForm(QtGui.QWidget):

    _path = DRIVERS_FORM

    def __init__(self):
        super(DriverForm, self).__init__()
        uic.loadUi(self._path, self)

    def get_data(self):
        pass

