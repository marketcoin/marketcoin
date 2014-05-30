from gui.marketcoin import Ui_MainWindow
from gui.payment_request import Ui_PaymentRequest
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time

# ui.setupUi(MainWindow)
# MainWindow.show()

#def update_state(ui):
#  # TODO: generic state update here.
#  print("TODO: update gui state")

def show_payment_request(label=None, message=None):
  Dialog = QtWidgets.QDialog()
  payment_request = Ui_PaymentRequest()
  payment_request.setupUi(Dialog)
  Dialog.exec_()

def setup_buttons(ui):
  ui.generate_payment_request.clicked.connect(lambda: show_payment_request())

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
