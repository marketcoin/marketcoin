# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payment_request.ui'
#
# Created: Thu Jun 19 19:51:31 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PaymentRequest(object):
    def setupUi(self, PaymentRequest):
        PaymentRequest.setObjectName("PaymentRequest")
        PaymentRequest.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(PaymentRequest)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(PaymentRequest)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout.addWidget(self.plainTextEdit_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(PaymentRequest)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PaymentRequest)
        self.buttonBox.accepted.connect(PaymentRequest.accept)
        self.buttonBox.rejected.connect(PaymentRequest.reject)
        QtCore.QMetaObject.connectSlotsByName(PaymentRequest)

    def retranslateUi(self, PaymentRequest):
        _translate = QtCore.QCoreApplication.translate
        PaymentRequest.setWindowTitle(_translate("PaymentRequest", "Payment Request"))

