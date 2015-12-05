import os
import hashlib

from PyQt4 import QtCore, QtGui, uic
from windows.widgets import LOGIN_WIDGET


class LoginWidget(QtGui.QWidget):

    _path = LOGIN_WIDGET
    
    def __init__(self):
        super(LoginWidget, self).__init__()
        uic.loadUi(self._path, self)
        self.show()

        self.sign_in.clicked.connect(self.handle_sign_in)
        self.sign_up.clicked.connect(self.handle_sign_up)

    def handle_sign_in(self):
        login = self.login_field.toPlainText()
        password = self.password_field.toPlainText()
        hash = hashlib.sha224(password).hexdigest()
        # get user and compare values
        if False:
            self.parent.successful_sign_in()
        else:
            self.error_label.setText('Check your login and password.')

    def handle_sign_up(self):
        pass
