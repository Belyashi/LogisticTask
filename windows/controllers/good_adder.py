from PyQt4 import QtGui, QtCore, uic
from windows.widgets import ADD_GOOD_FORM


class GoodAdder(QtGui.QWidget):

    _path = ADD_GOOD_FORM

    def __init__(self, stacked_widget, *args, **kwargs):
        super(GoodAdder, self).__init__(*args, **kwargs)
        uic.loadUi(self._path, self)
        stacked_widget.addWidget(self)
        self.ancestor = args[0]

        self.add.clicked.connect(self.on_add)
        self.cancel.clicked.connect(self.on_cancel)

    def on_cancel(self):
        self.ancestor.on_cancel()

    def on_add(self):
        pass
        # validation of data in form and creating good
