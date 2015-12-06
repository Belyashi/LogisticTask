from PyQt4 import QtGui, uic

from windows.controllers.organization_interface.orders_adder import OrderAdder
from windows.widgets.path import ORGANiZATION_ORDERS


class OrdersView(QtGui.QWidget):

    _path = ORGANiZATION_ORDERS

    def __init__(self, stacked_widget, *args, **kwargs):
        super(OrdersView, self).__init__(*args, **kwargs)
        uic.loadUi(self._path, self)
        self.stacked_widget = stacked_widget
        self.stacked_widget.addWidget(self)
        self.ancestor = args[0]
        self.organization = self.ancestor.organization
        self.organization_id = self.ancestor.organization_id
        self.orders_adder = OrderAdder(stacked_widget, self)

        self.add.clicked.connect(self.add_order)
        self.back.clicked.connect(self.on_back)

    def on_cancel(self):
        self.stacked_widget.setCurrentWidget(self)

    def add_order(self):
        self.stacked_widget.setCurrentWidget(self.orders_adder)

    def on_back(self):
        self.ancestor.on_back()
