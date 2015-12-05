import os
import hashlib
from PyQt4 import QtCore, QtGui, uic


class LoginWidget(QtGui.QWidget):

    _file_name = 'login_widget.ui'
    _path = '/'.join(os.path.abspath(__file__).split('/')[:-1] + [_file_name])
    
    def __init__(self):
        super(LoginWidget, self).__init__()
        uic.loadUi('windows/widgets/login_widget.ui', self)
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
