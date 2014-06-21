from gui.marketcoin import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
import wallet


my_wallet = wallet.Wallet()


class TransactionTable(QtCore.QAbstractTableModel):
    COLUMNS = ['txid', 'to', 'amount']

    def headerData(self, index: int, orientation: QtCore.Qt.Orientation, role: int=None):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.COLUMNS[index]
        return QtCore.QVariant()

    def rowCount(self, parent: QtCore.QModelIndex=None, *args, **kwargs):
        return len([])

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self.COLUMNS)

    def data(self, index: QtCore.QModelIndex, role: int=None):
        if role == QtCore.Qt.DisplayRole:
            return 'cell'
        return QtCore.QVariant()

def do_send(ui: Ui_MainWindow):
    amount = int(ui.send_amount.text())
    recipient = str(ui.recipient.text())
    my_wallet.send(recipient, amount)


def setup_buttons(ui):
    ui.generate_payment_request.clicked.connect(
        lambda: ui.address.setText(my_wallet.generate_address(ui.label.text().strip())))
    transaction_table = TransactionTable()
    ui.transactions.setModel(transaction_table)
    ui.transactions_2.setModel(transaction_table)
    ui.send.clicked.connect(lambda: do_send(ui))


class StateUpdater(QtCore.QThread):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        # TODO

    def run(self):
        while True:
            self.ui.balance.setText(str(my_wallet.balance()))
            time.sleep(2)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

setup_buttons(ui)

state_updater = StateUpdater(ui)
state_updater.start()

sys.exit(app.exec_())
