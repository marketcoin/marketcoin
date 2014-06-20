from gui.marketcoin import Ui_MainWindow
from gui.payment_request import Ui_PaymentRequest
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ecdsa
import time
import random
import binascii

# ui.setupUi(MainWindow)
# MainWindow.show()

#def update_state(ui):
#  # TODO: generic state update here.
#  print("TODO: update gui state")

system_random = random.SystemRandom()


def key_to_string(key):
    return binascii.hexlify(key.to_string()).decode('utf-8')


class TransactionTable(QtCore.QAbstractTableModel):

    def headerData(self, p_int, orientation: QtCore.Qt.Orientation, int_role=None):
        if orientation == QtCore.Qt.Horizontal and int_role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant("Column" + str(p_int))
        return QtCore.QVariant()

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return 5

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs):
        return 4

    def data(self, index: QtCore.QModelIndex, int_role: int=None):
        if int_role == QtCore.Qt.DisplayRole:
            return "Row%d, Column%d"%(index.row(), index.column())
        return QtCore.QVariant()


def generate_address(output: QtWidgets.QLineEdit, label: str):
    # TODO: introduce extra entropy
    secret = system_random.randrange(ecdsa.SECP256k1.order)
    private_key = ecdsa.SigningKey.from_secret_exponent(secret, curve=ecdsa.SECP256k1)
    with open("keys.txt", "ab") as f:
        f.write(key_to_string(private_key).encode('utf-8') + b':' + label.encode('utf-8') + b'\n')
    public_key = private_key.get_verifying_key()
    output.setText(key_to_string(public_key))


def setup_buttons(ui):
    ui.generate_payment_request.clicked.connect(lambda: generate_address(ui.address, ui.label.text()))
    transaction_table = TransactionTable()
    ui.transactions.setModel(transaction_table)
    ui.transactions_2.setModel(transaction_table)


"""
class StateUpdater(QtCore.QThread):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        # TODO

    def run(self):
        while True:
            update_state(self.ui)
            time.sleep(2)
"""

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

setup_buttons(ui)

#state_updater = StateUpdater(ui)
#state_updater.start()

sys.exit(app.exec_())
