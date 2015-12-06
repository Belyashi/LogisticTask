from PyQt4 import QtGui, QtCore, uic
from windows.widgets import DRIVER_INTERFACE
from models.drivers import Drivers
from models.map import Map


class DriverInterface(QtGui.QWidget):

    _path = DRIVER_INTERFACE

    def __init__(self, user_id, *args, **kwargs):
        super(DriverInterface, self).__init__(*args, **kwargs)
        uic.loadUi(self._path, self)
        self.model = QtGui.QStandardItemModel()
        self.orders.setModel(self.model)
        self.driver = Drivers()
        self.driver_id = self.driver.get_driver_id(user_id)
        self.set_curent_info()

        self.notifier.clicked.connect(self.change_state)

    def set_current_info(self):
        current_way = self.driver.get_next_point(self.driver_id)
        finish_city = current_way['finish_city']
        self.driver.get_driver_info(self.driver_id)

    def change_state(self):
        pass

