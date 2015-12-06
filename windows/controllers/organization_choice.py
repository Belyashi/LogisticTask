from PyQt4 import QtCore, QtGui, uic
from windows.widgets.path import ORGANIZATION_CHOICE
from windows.controllers.goods_view import GoodsView
from windows.controllers.orders_view import OrdersView


class OrganizationChoice(QtGui.QWidget):

    _path = ORGANIZATION_CHOICE

    def __init__(self, stacked_widget, *args, **kwargs):
        super(OrganizationChoice, self).__init__(*args, **kwargs)
        uic.loadUi(self._path, self)
        self.stacked_widget = stacked_widget
        self.stacked_widget.addWidget(self)
        self.ancestor = args[0]
        self.goods_view = GoodsView(self.stacked_widget, self)
        self.orders_view = OrdersView(self.stacked_widget, self)
        self.goods.clicked.connect(self.show_goods)
        self.orders.clicked.connect(self.show_orders)

    def show_goods(self):
        self.stacked_widget.setCurrentWidget(self.goods_view)

    def show_orders(self):
        self.stacked_widget.setCurrentWidget(self.orders_view)

    def on_back(self):
        self.stacked_widget.setCurrentWidget(self)
