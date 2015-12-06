from PyQt4 import QtGui, QtCore, uic
from windows.widgets import COMPANY_FORM


class CompanyForm(QtGui.QWidget):

    _path = COMPANY_FORM

    def __init__(self):
        super(CompanyForm, self).__init__()
        uic.loadUi(self._path, self)

    def get_data(self):
        name = self.company.toPlainText()
        location = self.location.toPlainText()
        # FIXME: add check for name uniqueness and location
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
