from gui.marketcoin import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time

def update_state(ui):
  # TODO: generic state update here.
  print("TODO: update gui state")

# TODO:
# ui.button.clicked.connect(lambda: handle_click(ui))

class StateUpdater(QtCore.QThread):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        # TODO

    def run(self):
        while True:
            update_state(self.ui)
            time.sleep(2)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

state_updater = StateUpdater(ui)
state_updater.start()

sys.exit(app.exec_())
