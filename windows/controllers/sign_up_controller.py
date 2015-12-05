from PyQt4 import QtCore, QtGui, uic
from windows.widgets import SIGN_UP_WIDGET
from driver_form import DriverForm
from company_form import CompanyForm


class SignUpWidget(QtGui.QWidget):

    _path = SIGN_UP_WIDGET

    def __init__(self, *args, **kwargs):
        super(SignUpWidget, self).__init__(*args, **kwargs)
        uic.loadUi(self._path, self)
        self.show()

        self.role_selector.currentIndexChanged\
            .connect(self.changed_role_selector)
        self._driver_form = DriverForm()
        self._company_form = CompanyForm()
        self.additional_data.addWidget(self._driver_form)
        self.additional_data.addWidget(self._company_form)
        self.role_selector.setCurrentIndex(0)
        self.changed_role_selector(0)
        self.sign_up.clicked.connect(self.sign_up_user)
        self.cancel.clicked.connect(self.cancel_sign_up)

    def changed_role_selector(self, index):
        role = self.role_selector.itemText(index)
        if role == 'Driver':
            self.additional_data.setCurrentWidget(self._driver_form)
        else:
            self.additional_data.setCurrentWidget(self._company_form)

    def sign_up_user(self):
        password = self.password_input.toPlainText()
        repeated_password = self.repeated_password.toPlainText()
        data = self.additional_data.currentWidget().get_data()
        if data['success'] and password == repeated_password:
            pass
            # Make registration
        else:
            self.error.setText('Something wrong with your form data.')

    def cancel_sign_up(self):
        self.parent().cancel_sign_up()
