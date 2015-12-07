from PyQt4 import QtGui, QtCore, uic
from windows.widgets import DRIVERS_FORM


class DriverForm(QtGui.QWidget):

    _path = DRIVERS_FORM

    def __init__(self):
        super(DriverForm, self).__init__()
        uic.loadUi(self._path, self)

    def get_data(self):
        try:
            capacity = int(self.capacity.text())
        except Exception:
            capacity = -1
        location = self.location.text()
        # FIXME: make normal check of location
        if capacity >= 1 and location:
            return {
                'success': True,
                'capacity': capacity,
                'location': location
            }
        else:
            return {
                'success': False
            }
