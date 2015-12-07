from PyQt4 import QtGui, uic

from windows.controllers.organization_interface.orders_adder import OrderAdder
from windows.widgets.path import ORGANiZATION_ORDERS
from models.organizations import Organizations


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
        self.column_index = {}
        self.model = QtGui.QStandardItemModel()
        self.update_info()
        self.orders_view.setModel(self.model)

        self.add.clicked.connect(self.add_order)
        self.back.clicked.connect(self.on_back)

    def on_cancel(self):
        self.update_info()
        self.stacked_widget.setCurrentWidget(self)

    def add_order(self):
        self.stacked_widget.setCurrentWidget(self.orders_adder)

    def on_back(self):
        self.ancestor.on_back()

    def update_info(self):
        orders = Organizations().get_orders(self.organization_id)
        # orders = filter(
        #     lambda x: x['producer_id'] == self.organization_id,
        #     orders
        # )
        # for order in orders:
        #     order.pop('producer_id')
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
