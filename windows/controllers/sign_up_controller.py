from PyQt4 import QtCore, QtGui, uic
from windows.widgets import SIGN_UP_WIDGET
from driver_form import DriverForm
from company_form import CompanyForm


class SignUpWidget(QtGui.QWidget):

    _path = SIGN_UP_WIDGET

    def __init__(self):
        super(SignUpWidget, self).__init__()
        uic.loadUi(self._path, self)
        self.show()

        self.role_selector.currentIndexChanged\
            .connect(self.changed_role_selector)
        self._driver_form = DriverForm()
        self._company_form = CompanyForm()
        self.additional_data.addWidget(self._driver_form)
        self.additional_data.addWidget(self._company_form)
        self.role_selector.setCurrentIndex(0)
        self.changed_role_selector(0)

    def changed_role_selector(self, index):
        role = self.role_selector.itemText(index)
        if role == 'Driver':
            self.additional_data.setCurrentWidget(self._driver_form)
        else:
            self.additional_data.setCurrentWidget(self._company_form)
