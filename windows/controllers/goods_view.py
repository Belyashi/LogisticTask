from PyQt4 import QtGui, QtCore, uic
from windows.widgets import ORGANIZATION_GOODS
from windows.controllers.good_adder import GoodAdder


class GoodsView(QtGui.QWidget):

    _path = ORGANIZATION_GOODS

    def __init__(self, stacked_widget, *args, **kwargs):
        super(GoodsView, self).__init__(*args, **kwargs)
        uic.loadUi(self._path, self)
        self.stacked_widget = stacked_widget
        self.stacked_widget.addWidget(self)
        self.ancestor = args[0]
        self.good_adder = GoodAdder(self.stacked_widget, self)

        self.back.clicked.connect(self.on_back)
        self.add.clicked.connect(self.add_good)

    def on_cancel(self):
        self.stacked_widget.setCurrentWidget(self)

    def on_back(self):
        self.ancestor.on_back()

    def add_good(self):
        self.stacked_widget.setCurrentWidget(self.good_adder)
