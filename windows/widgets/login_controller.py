from PyQt4 import QtCore, QtGui, uic


class LoginWidget(QtGui.QWidget):
    
    def __init__(self):
        super(LoginWidget, self).__init__()
        uic.loadUi('windows/widgets/login_widget.ui', self)
        self.show()
        self.sign_in.clicked.connect(self.handleLogIn)

    def handleLogIn(self):
        login = self.login_field.toPlainText()
        self.password_field.clear()
        self.password_field.insertPlainText(login)
