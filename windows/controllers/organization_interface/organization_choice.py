from PyQt4 import QtGui, uic

from windows.controllers.organization_interface import GoodsView

from windows.controllers.organization_interface import OrdersView
from windows.widgets.path import ORGANIZATION_CHOICE


class OrganizationChoice(QtGui.QWidget):

    _path = ORGANIZATION_CHOICE

    def __init__(self, stacked_widget, *args, **kwargs):
        super(OrganizationChoice, self).__init__(*args, **kwargs)
        uic.loadUi(self._path, self)
        self.stacked_widget = stacked_widget
        self.stacked_widget.addWidget(self)
        self.ancestor = args[0]
        self.organization = self.ancestor.organization
        self.organization_id = self.ancestor.organization_id
        self.goods_view = GoodsView(self.stacked_widget, self)
        self.orders_view = OrdersView(self.stacked_widget, self)
        self.goods.clicked.connect(self.show_goods)
        self.orders.clicked.connect(self.show_orders)

    def show_goods(self):
        self.goods_view.update_info()
        self.stacked_widget.setCurrentWidget(self.goods_view)

    def show_orders(self):
        #self.orders_view.update_info()
        self.stacked_widget.setCurrentWidget(self.orders_view)

    def on_back(self):
        self.stacked_widget.setCurrentWidget(self)
