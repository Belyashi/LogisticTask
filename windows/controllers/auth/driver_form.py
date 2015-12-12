from PyQt4 import QtGui, QtCore, uic
from windows.widgets import DRIVERS_FORM
from models.map import Map


class DriverForm(QtGui.QWidget):

    _path = DRIVERS_FORM

    def __init__(self):
        super(DriverForm, self).__init__()
        uic.loadUi(self._path, self)
        self.cities = Map().get_all_cities()
        self.location.clear()
        for city in self.cities:
            self.location.addItem(city['name'])

    def get_data(self):
        try:
            capacity = int(self.capacity.text())
        except Exception:
            capacity = -1
        location = self.location.currentIndex()
        location = self.cities[location]['id']
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
