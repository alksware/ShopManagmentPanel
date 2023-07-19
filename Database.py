import sqlite3
from projectUI import Ui_MainWindow
from projectUI import Ui_MainWindow
import sqlite3

ui = Ui_MainWindow()
ui.setupUi()


class Database:
    con = sqlite3.connect("applicationDB.db")
    cursor = con.cursor()

    def createTable(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS applicationTable (
            productCode INT,
            productName TEXT,
            productAmount INT,
            productPrice INT,
            productDescription TEXT,
            productCategory TEXT,
            productBrand TEXT
        )""")
        self.con.commit()


def addProduct(self):
    productCode = int(self.ui.productCode.text())
    productName = self.ui.productName.text()
    productAmount = int(self.ui.productAmount.text())
    productPrice = float(self.ui.productPrice.text())
    productDescription = self.ui.productDescription.text()
    productCategory = self.ui.cmdCatagory.currentText()
    productBrand = self.ui.cmbProduct.currentText()

    Query = (
        "insert into applicationTable values(?,?,?,?,?,?,?)",
        productCode,
        productName,
        productAmount,
        productPrice,
        productDescription,
        productCategory,
        productBrand)

    try:
        self.cursor.execute(*Query)
        self.con.commit()
        self.ui.statusbar.showMessage("Product Added", 1000)
    except Exception as ex:
        self.ui.statusbar.showMessage("Product Couldn't be Added", 1000)
        raise ex


db = Database()
