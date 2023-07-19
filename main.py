import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from projectUI import Ui_MainWindow
from Database import *

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

databaseClass = Database()
ui.addProductButton.clicked.connect(databaseClass.addProduct)

window.show()
sys.exit(app.exec_())
