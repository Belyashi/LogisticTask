from PyQt4 import QtGui, QtCore, uic
from windows.widgets.path import ADD_ORDER_FORM
from models.organizations import Organizations
from models.goods import Goods


class OrderAdder(QtGui.QWidget):

    _path = ADD_ORDER_FORM

    def __init__(self, stacked_widget, *args, **kwargs):
        super(OrderAdder, self).__init__(*args, **kwargs)
        uic.loadUi(self._path, self)
        stacked_widget.addWidget(self)
        self.ancestor = args[0]
        self.organization = Organizations()
        self.goods = Goods().get_all_goods()
        self.update_data()

        self.add.clicked.connect(self.on_add)
        self.cancel.clicked.connect(self.on_cancel)
        self.good_list.currentRowChanged.connect(self.good_changed)

    def on_cancel(self):
        self.ancestor.on_cancel()

    def on_add(self):
        try:
            selected_good = self.goods[self.good_list.currentRow() - 1]
            good_id = selected_good['id']
            count = int(self.count.text())
            if count > selected_good['residue']:
                self.error.setText('Wrong good count.')
            else:
                self.organization.add_order(
                    self.ancestor.organization_id,
                    good_id,
                    count
                )
            Goods().reduce(good_id, count)
        except Exception as e:
            self.error.setText('Something wrong with data.')
        finally:
            self.update_data()

    def update_data(self):
        self.good_list.clear()
        self.goods = Goods().get_all_goods()
        writen_keys = False
        for good in self.goods:
            values = []
            keys = []
            for key, value in good.iteritems():
                if key != 'producer_id':
                    keys.append(key)
                    values.append(str(value))
            if not writen_keys:
                writen_keys = True
                self.good_list.addItem('\t '.join(keys))
            self.good_list.addItem('\t'.join(values))

    def good_changed(self, index):
        if index == -1:
            return
        try:
            self.error.setText('')
            if index <= 0:
                raise ValueError
            self.good_id.setText(str(self.goods[index - 1]['id']))
        except Exception as e:
            self.error.setText('Do not choose this option.')
