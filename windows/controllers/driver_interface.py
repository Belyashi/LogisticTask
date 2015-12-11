from PyQt4 import QtGui, QtCore, uic
from windows.widgets import DRIVER_INTERFACE
from models.drivers import Drivers
from models.map import Map


class DriverInterface(QtGui.QWidget):

    _path = DRIVER_INTERFACE

    def __init__(self, user_id, *args, **kwargs):
        super(DriverInterface, self).__init__(*args, **kwargs)
        uic.loadUi(self._path, self)
        self.driver = Drivers()
        self.driver_id = self.driver.get_driver_id(user_id)
        self.is_moving = None
        self.model = QtGui.QStandardItemModel()
        self.orders.setModel(self.model)
        self.set_current_info()

        self.notifier.clicked.connect(self.change_state)

    def set_current_info(self):
        current_way = self.driver.get_next_point(self.driver_id)
        finish_city = current_way['finish_city'] if current_way else ''
        driver_info = self.driver.get_driver_info(self.driver_id)
        if True:  # driver_info['on_way']:
            self.is_moving = True
            self.notifier.setText('Arrive')
        else:
            self.is_moving = False
            self.notifier.setText('Start')
        self.update_state()

    def change_state(self):
        if self.is_moving:
            self.driver.arrive_to_point(self.driver_id)
            self.set_current_info()
        else:
            self.driver.start_move(self.driver_id)
            self.set_current_info()

    def update_state(self):
        orders = self.driver.get_orders(self.driver_id)
        self.model.clear()
        header_labels = [key for key in orders[0]] if len(orders) > 0 else\
            ['id']
        self.model.setHorizontalHeaderLabels(header_labels)
        row_count = 0
        for order in orders:
            column_count = 0
            for key, value in order.iteritems():
                self.model.setItem(row_count, column_count,
                                   QtGui.QStandardItem(str(value)))
                column_count += 1
            row_count += 1
