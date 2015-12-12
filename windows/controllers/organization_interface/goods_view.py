from PyQt4 import QtGui, uic

from models.goods import Goods
from windows.controllers.organization_interface.good_adder import GoodAdder
from windows.widgets import ORGANIZATION_GOODS


class GoodsView(QtGui.QWidget):

    _path = ORGANIZATION_GOODS

    def __init__(self, stacked_widget, *args, **kwargs):
        super(GoodsView, self).__init__(*args, **kwargs)
        uic.loadUi(self._path, self)
        self.stacked_widget = stacked_widget
        self.stacked_widget.addWidget(self)
        self.ancestor = args[0]
        self.organization = self.ancestor.organization
        self.organization_id = self.ancestor.organization_id
        self.good_adder = GoodAdder(self.stacked_widget, self)
        self.column_index = {}
        self.model = QtGui.QStandardItemModel()
        self.update_info()
        self.goods_view.setModel(self.model)

        self.back.clicked.connect(self.on_back)
        self.add.clicked.connect(self.add_good)

    def on_cancel(self):
        self.update_info()
        self.stacked_widget.setCurrentWidget(self)

    def on_back(self):
        self.ancestor.on_back()

    def add_good(self):
        self.stacked_widget.setCurrentWidget(self.good_adder)

    def update_info(self):
        goods = Goods().get_all_goods()
        goods = filter(
            lambda x: x['producer_id'] == self.organization_id,
            goods
        )
        for good in goods:
            good.pop('producer_id')
        self.model.clear()
        header_labels = [key for key in goods[0] if key != 'id'] if len(goods) > 0 else\
            ['name', 'weight', 'price', 'residue']
        self.model.setHorizontalHeaderLabels(header_labels)
        row_count = 0
        for good in goods:
            column_count = 0
            for key, value in good.iteritems():
                if key != 'id':
                    self.model.setItem(row_count, column_count,
                                  QtGui.QStandardItem(str(value)))
                    column_count += 1
            row_count += 1
