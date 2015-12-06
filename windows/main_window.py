from PyQt4 import QtGui

from windows.controllers import LoginWidget, SignUpWidget, \
    OrganizationInterface,DriverInterface
from models.users import Users


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setGeometry(600, 300, 500, 100)
        self.setWindowTitle('Logistic Task')

        self.setCentralWidget(LoginWidget(self))

    def sign_up_user(self):
        self.setCentralWidget(SignUpWidget(self))

    def close_sign_up(self):
        self.setCentralWidget(LoginWidget(self))

    def successful_sign_in(self, user_id):
        user = Users()
        if user.is_driver(user_id):
            self.setCentralWidget(DriverInterface(user_id, self))
        if user.is_organization(user_id):
            self.setCentralWidget(OrganizationInterface(user_id, self))
