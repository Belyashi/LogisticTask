from PyQt4 import QtGui, QtCore, uic
from windows.widgets import ADD_GOOD_FORM
from models.organizations import Organizations


class GoodAdder(QtGui.QWidget):

    _path = ADD_GOOD_FORM

    def __init__(self, stacked_widget, *args, **kwargs):
        super(GoodAdder, self).__init__(*args, **kwargs)
        uic.loadUi(self._path, self)
        stacked_widget.addWidget(self)
        self.ancestor = args[0]
        self.organization = Organizations()

        self.add.clicked.connect(self.on_add)
        self.cancel.clicked.connect(self.on_cancel)

    def on_cancel(self):
        self.ancestor.on_cancel()

    def on_add(self):
        name = self.name.text()
        price = self.price.text()
        weight = self.weight.text()
        residue = self.residue.text()
        try:
            price = int(price)
            weight = int(weight)
            residue = int(residue)
            self.organization.add_goods(
                name,
                price,
                self.ancestor.organization_id,
                residue,
                weight
            )
            self.on_cancel()
            return
        except Exception as e:
            self.error.setText('Something wrong with good.')

