from PyQt4 import QtCore, QtGui
from widgets.login_controller import LoginWidget


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setGeometry(600, 300, 500, 100)
        self.setWindowTitle("Logistic Task")

        login_widget = LoginWidget()
        login_widget.setParent(self)
        self.setCentralWidget(login_widget)
