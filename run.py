import sys
from PyQt4 import QtCore, QtGui

from windows.main_window import MainWindow


app = QtGui.QApplication(sys.argv)
mw = MainWindow()
mw.show()
app.exec_()


