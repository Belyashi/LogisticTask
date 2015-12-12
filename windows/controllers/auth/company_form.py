from PyQt4 import QtGui, QtCore, uic
from windows.widgets import COMPANY_FORM
from models.map import Map


class CompanyForm(QtGui.QWidget):

    _path = COMPANY_FORM

    def __init__(self):
        super(CompanyForm, self).__init__()
        uic.loadUi(self._path, self)
        self.cities = Map().get_all_cities()
        self.location.clear()
        for city in self.cities:
            self.location.addItem(city['name'])

    def get_data(self):
        name = self.company.text()
        location = self.location.currentIndex()
        location = self.cities[location]['id']
        if name and location:
            return {
                'success': True,
                'name': name,
                'location': location
            }
        else:
            return {
                'success': False
            }
