# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backgroundworker.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_diag_backgroundworker(object):
    def setupUi(self, diag_backgroundworker):
        diag_backgroundworker.setObjectName("diag_backgroundworker")
        diag_backgroundworker.resize(418, 97)
        diag_backgroundworker.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(diag_backgroundworker)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_status = QtWidgets.QLabel(diag_backgroundworker)
        self.lbl_status.setText("Status message...")
        self.lbl_status.setObjectName("lbl_status")
        self.verticalLayout.addWidget(self.lbl_status)
        self.pgb_status = QtWidgets.QProgressBar(diag_backgroundworker)
        self.pgb_status.setMinimumSize(QtCore.QSize(400, 0))
        self.pgb_status.setObjectName("pgb_status")
        self.verticalLayout.addWidget(self.pgb_status)
        self.btn_box = QtWidgets.QDialogButtonBox(diag_backgroundworker)
        self.btn_box.setOrientation(QtCore.Qt.Horizontal)
        self.btn_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.btn_box.setCenterButtons(True)
        self.btn_box.setObjectName("btn_box")
        self.verticalLayout.addWidget(self.btn_box)

        self.retranslateUi(diag_backgroundworker)
        QtCore.QMetaObject.connectSlotsByName(diag_backgroundworker)

    def retranslateUi(self, diag_backgroundworker):
        _translate = QtCore.QCoreApplication.translate
        diag_backgroundworker.setWindowTitle(_translate("diag_backgroundworker", "File transfer..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    diag_backgroundworker = QtWidgets.QDialog()
    ui = Ui_diag_backgroundworker()
    ui.setupUi(diag_backgroundworker)
    diag_backgroundworker.show()
    sys.exit(app.exec_())
