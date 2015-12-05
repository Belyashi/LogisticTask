from PyQt4 import QtGui

from windows.controllers import LoginWidget, SignUpWidget


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setGeometry(600, 300, 500, 100)
        self.setWindowTitle('Logistic Task')

        login_widget = SignUpWidget()
        login_widget.setParent(self)
        self.setCentralWidget(login_widget)
