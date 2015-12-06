from PyQt4 import QtGui, QtCore, uic
from windows.widgets.path import ADD_ORDER_FORM


class OrderAdder(QtGui.QWidget):

    _path = ADD_ORDER_FORM

    def __init__(self, stacked_widget, *args, **kwargs):
        super(OrderAdder, self).__init__(*args, **kwargs)
        uic.loadUi(self._path, self)
        stacked_widget.addWidget(self)
        self.ancestor = args[0]

        self.add.clicked.connect(self.on_add)
        self.cancel.clicked.connect(self.on_cancel)

    def on_cancel(self):
        self.ancestor.on_cancel()

    def on_add(self):
        pass
    # TODO: make validation and creation
