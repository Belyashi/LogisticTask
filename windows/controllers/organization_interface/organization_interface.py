from PyQt4 import QtGui, QtCore, uic
from windows.widgets import ORGANIZATION_INTERFACE
from windows.controllers.organization_interface import OrganizationChoice
from models.organizations import Organizations


class OrganizationInterface(QtGui.QWidget):

    _path = ORGANIZATION_INTERFACE

    def __init__(self, user_id, *args, **kwargs):
        super(OrganizationInterface, self).__init__(*args, **kwargs)
        uic.loadUi(self._path, self)
        self.organization = Organizations()
        self.organization_id = self.organization.get_organization_id(user_id)
        self.choice = OrganizationChoice(self.interfaces, self)
        self.interfaces.setCurrentWidget(self.choice)
