from PyQt4 import QtGui

from windows.controllers import LoginWidget, SignUpWidget


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
