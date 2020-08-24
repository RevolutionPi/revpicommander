# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'revpiinfo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_diag_revpiinfo(object):
    def setupUi(self, diag_revpiinfo):
        diag_revpiinfo.setObjectName("diag_revpiinfo")
        diag_revpiinfo.resize(627, 398)
        self.gridLayout = QtWidgets.QGridLayout(diag_revpiinfo)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_head = QtWidgets.QLabel(diag_revpiinfo)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_head.setFont(font)
        self.lbl_head.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_head.setObjectName("lbl_head")
        self.gridLayout.addWidget(self.lbl_head, 0, 0, 1, 3)
        self.lbl_lbl_version_pyload = QtWidgets.QLabel(diag_revpiinfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_lbl_version_pyload.setFont(font)
        self.lbl_lbl_version_pyload.setObjectName("lbl_lbl_version_pyload")
        self.gridLayout.addWidget(self.lbl_lbl_version_pyload, 3, 0, 1, 1)
        self.lst_files = QtWidgets.QListWidget(diag_revpiinfo)
        self.lst_files.setObjectName("lst_files")
        self.gridLayout.addWidget(self.lst_files, 3, 2, 4, 1)
        self.lbl_version_pyload = QtWidgets.QLabel(diag_revpiinfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_version_pyload.setFont(font)
        self.lbl_version_pyload.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_version_pyload.setObjectName("lbl_version_pyload")
        self.gridLayout.addWidget(self.lbl_version_pyload, 3, 1, 1, 1)
        self.lbl_link = QtWidgets.QLabel(diag_revpiinfo)
        self.lbl_link.setOpenExternalLinks(True)
        self.lbl_link.setObjectName("lbl_link")
        self.gridLayout.addWidget(self.lbl_link, 6, 0, 1, 1)
        self.btn_box = QtWidgets.QDialogButtonBox(diag_revpiinfo)
        self.btn_box.setOrientation(QtCore.Qt.Horizontal)
        self.btn_box.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.btn_box.setObjectName("btn_box")
        self.gridLayout.addWidget(self.btn_box, 7, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_lbl_version_control = QtWidgets.QLabel(diag_revpiinfo)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_lbl_version_control.setFont(font)
        self.lbl_lbl_version_control.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_lbl_version_control.setObjectName("lbl_lbl_version_control")
        self.horizontalLayout.addWidget(self.lbl_lbl_version_control)
        self.lbl_version_control = QtWidgets.QLabel(diag_revpiinfo)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_version_control.setFont(font)
        self.lbl_version_control.setObjectName("lbl_version_control")
        self.horizontalLayout.addWidget(self.lbl_version_control)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 3)
        self.lbl_info = QtWidgets.QLabel(diag_revpiinfo)
        self.lbl_info.setMinimumSize(QtCore.QSize(300, 0))
        self.lbl_info.setWordWrap(True)
        self.lbl_info.setObjectName("lbl_info")
        self.gridLayout.addWidget(self.lbl_info, 4, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)

        self.retranslateUi(diag_revpiinfo)
        self.btn_box.accepted.connect(diag_revpiinfo.accept)
        self.btn_box.rejected.connect(diag_revpiinfo.reject)
        QtCore.QMetaObject.connectSlotsByName(diag_revpiinfo)

    def retranslateUi(self, diag_revpiinfo):
        _translate = QtCore.QCoreApplication.translate
        diag_revpiinfo.setWindowTitle(_translate("diag_revpiinfo", "Dialog"))
        self.lbl_head.setText(_translate("diag_revpiinfo", "RevPi Python PLC - Control"))
        self.lbl_lbl_version_pyload.setText(_translate("diag_revpiinfo", "RevPiPyLoad version on RevPi:"))
        self.lbl_version_pyload.setText(_translate("diag_revpiinfo", "0.0.0"))
        self.lbl_link.setText(_translate("diag_revpiinfo", "<html><head/><body><p><a href=\"https://revpimodio.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">https://revpimodio.org/</span></a></p></body></html>"))
        self.lbl_lbl_version_control.setText(_translate("diag_revpiinfo", "Version:"))
        self.lbl_version_control.setText(_translate("diag_revpiinfo", "0.0.0"))
        self.lbl_info.setText(_translate("diag_revpiinfo", "RevPiModIO, RevPiPyLoad and RevPiPyControl are community driven projects. They are all free and open source software.\n"
"All of them comes with ABSOLUTELY NO WARRANTY, to the extent permitted by\n"
"applicable law.\n"
"\n"
"(c) Sven Sager, License: GPLv3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    diag_revpiinfo = QtWidgets.QDialog()
    ui = Ui_diag_revpiinfo()
    ui.setupUi(diag_revpiinfo)
    diag_revpiinfo.show()
    sys.exit(app.exec_())

