import os
import hashlib

from PyQt4 import QtCore, QtGui, uic
from windows.widgets import LOGIN_WIDGET
from models.users import Users


class LoginWidget(QtGui.QWidget):

    _path = LOGIN_WIDGET
    
    def __init__(self, *args, **kwargs):
        super(LoginWidget, self).__init__(*args, **kwargs)
        uic.loadUi(self._path, self)
        self.show()

        self.users = Users()
        self.sign_in.clicked.connect(self.handle_sign_in)
        self.sign_up.clicked.connect(self.handle_sign_up)

    def handle_sign_in(self):
        login = self.login_field.text()
        password = self.password_field.text()
        password = hashlib.sha224(password).hexdigest()
        try:
            result = self.users.login(login, password)
        except ValueError as v:
            # TODO: change it on 'Login or password is incorrect.'
            self.error_label.setText(v.message)
            result = False
        if result:
            self.parent().successful_sign_in(result)

    def handle_sign_up(self):
        self.parent().sign_up_user()
