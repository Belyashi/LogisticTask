from PyQt4 import QtGui, QtCore, uic
from windows.widgets import ORGANIZATION_INTERFACE
from windows.controllers import OrganizationChoice


class OrganizationInterface(QtGui.QWidget):

    _path = ORGANIZATION_INTERFACE

    def __init__(self, *args, **kwargs):
        super(OrganizationInterface, self).__init__(*args, **kwargs)
        uic.loadUi(self._path, self)
        self.choice = OrganizationChoice(self.interfaces, self)
        self.interfaces.setCurrentWidget(self.choice)
