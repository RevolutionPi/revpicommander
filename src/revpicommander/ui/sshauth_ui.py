# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sshauth.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_diag_sshauth(object):
    def setupUi(self, diag_sshauth):
        diag_sshauth.setObjectName("diag_sshauth")
        diag_sshauth.setWindowModality(QtCore.Qt.ApplicationModal)
        diag_sshauth.resize(331, 225)
        self.verticalLayout = QtWidgets.QVBoxLayout(diag_sshauth)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wid_password = QtWidgets.QWidget(diag_sshauth)
        self.wid_password.setObjectName("wid_password")
        self.formLayout = QtWidgets.QFormLayout(self.wid_password)
        self.formLayout.setObjectName("formLayout")
        self.lbl_username = QtWidgets.QLabel(self.wid_password)
        self.lbl_username.setObjectName("lbl_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_username)
        self.lbl_password = QtWidgets.QLabel(self.wid_password)
        self.lbl_password.setObjectName("lbl_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_password)
        self.txt_password = QtWidgets.QLineEdit(self.wid_password)
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName("txt_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_password)
        self.txt_username = QtWidgets.QLineEdit(self.wid_password)
        self.txt_username.setObjectName("txt_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_username)
        self.verticalLayout.addWidget(self.wid_password)
        self.cbx_save_password = QtWidgets.QCheckBox(diag_sshauth)
        self.cbx_save_password.setObjectName("cbx_save_password")
        self.verticalLayout.addWidget(self.cbx_save_password)
        self.btn_box = QtWidgets.QDialogButtonBox(diag_sshauth)
        self.btn_box.setOrientation(QtCore.Qt.Horizontal)
        self.btn_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_box.setObjectName("btn_box")
        self.verticalLayout.addWidget(self.btn_box)
        self.lbl_info = QtWidgets.QLabel(diag_sshauth)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_info.sizePolicy().hasHeightForWidth())
        self.lbl_info.setSizePolicy(sizePolicy)
        self.lbl_info.setWordWrap(True)
        self.lbl_info.setObjectName("lbl_info")
        self.verticalLayout.addWidget(self.lbl_info)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(diag_sshauth)
        self.btn_box.accepted.connect(diag_sshauth.accept) # type: ignore
        self.btn_box.rejected.connect(diag_sshauth.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(diag_sshauth)

    def retranslateUi(self, diag_sshauth):
        _translate = QtCore.QCoreApplication.translate
        diag_sshauth.setWindowTitle(_translate("diag_sshauth", "SSH authentication"))
        self.lbl_username.setText(_translate("diag_sshauth", "SSH username:"))
        self.lbl_password.setText(_translate("diag_sshauth", "SSH password:"))
        self.cbx_save_password.setToolTip(_translate("diag_sshauth", "Username and password will be saved in secured operating systems\'s password storage."))
        self.cbx_save_password.setText(_translate("diag_sshauth", "Save username and password"))
        self.lbl_info.setText(_translate("diag_sshauth", "Note: The default user for SSH is \"pi\" which differs from the web configuration. You can find the password on the sticker on the device."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    diag_sshauth = QtWidgets.QDialog()
    ui = Ui_diag_sshauth()
    ui.setupUi(diag_sshauth)
    diag_sshauth.show()
    sys.exit(app.exec_())
