# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'revpioption.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_diag_options(object):
    def setupUi(self, diag_options):
        diag_options.setObjectName("diag_options")
        diag_options.resize(458, 557)
        self.verticalLayout = QtWidgets.QVBoxLayout(diag_options)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gb_plc = QtWidgets.QGroupBox(diag_options)
        self.gb_plc.setObjectName("gb_plc")
        self.gridLayout = QtWidgets.QGridLayout(self.gb_plc)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_replace_io = QtWidgets.QLabel(self.gb_plc)
        self.lbl_replace_io.setObjectName("lbl_replace_io")
        self.gridLayout.addWidget(self.lbl_replace_io, 6, 0, 1, 1)
        self.cbx_zeroonerror = QtWidgets.QCheckBox(self.gb_plc)
        self.cbx_zeroonerror.setObjectName("cbx_zeroonerror")
        self.gridLayout.addWidget(self.cbx_zeroonerror, 5, 1, 1, 2)
        self.cbx_autostart = QtWidgets.QCheckBox(self.gb_plc)
        self.cbx_autostart.setObjectName("cbx_autostart")
        self.gridLayout.addWidget(self.cbx_autostart, 0, 0, 1, 3)
        self.cbb_reset_driver_action = QtWidgets.QComboBox(self.gb_plc)
        self.cbb_reset_driver_action.setObjectName("cbb_reset_driver_action")
        self.cbb_reset_driver_action.addItem("")
        self.cbb_reset_driver_action.addItem("")
        self.cbb_reset_driver_action.addItem("")
        self.gridLayout.addWidget(self.cbb_reset_driver_action, 8, 1, 1, 2)
        self.lbl_reset_driver_action = QtWidgets.QLabel(self.gb_plc)
        self.lbl_reset_driver_action.setObjectName("lbl_reset_driver_action")
        self.gridLayout.addWidget(self.lbl_reset_driver_action, 8, 0, 1, 1)
        self.lbl_plc_zero = QtWidgets.QLabel(self.gb_plc)
        self.lbl_plc_zero.setObjectName("lbl_plc_zero")
        self.gridLayout.addWidget(self.lbl_plc_zero, 3, 0, 1, 3)
        self.cbb_replace_io = QtWidgets.QComboBox(self.gb_plc)
        self.cbb_replace_io.setObjectName("cbb_replace_io")
        self.cbb_replace_io.addItem("")
        self.cbb_replace_io.addItem("")
        self.cbb_replace_io.addItem("")
        self.cbb_replace_io.addItem("")
        self.gridLayout.addWidget(self.cbb_replace_io, 6, 1, 1, 2)
        self.cbx_zeroonexit = QtWidgets.QCheckBox(self.gb_plc)
        self.cbx_zeroonexit.setObjectName("cbx_zeroonexit")
        self.gridLayout.addWidget(self.cbx_zeroonexit, 4, 1, 1, 2)
        self.lbl_plc_delay = QtWidgets.QLabel(self.gb_plc)
        self.lbl_plc_delay.setObjectName("lbl_plc_delay")
        self.gridLayout.addWidget(self.lbl_plc_delay, 2, 0, 1, 2)
        self.sbx_autoreloaddelay = QtWidgets.QSpinBox(self.gb_plc)
        self.sbx_autoreloaddelay.setMinimum(5)
        self.sbx_autoreloaddelay.setMaximum(120)
        self.sbx_autoreloaddelay.setObjectName("sbx_autoreloaddelay")
        self.gridLayout.addWidget(self.sbx_autoreloaddelay, 2, 2, 1, 1)
        self.cbx_autoreload = QtWidgets.QCheckBox(self.gb_plc)
        self.cbx_autoreload.setObjectName("cbx_autoreload")
        self.gridLayout.addWidget(self.cbx_autoreload, 1, 0, 1, 3)
        self.txt_replace_io = QtWidgets.QLineEdit(self.gb_plc)
        self.txt_replace_io.setObjectName("txt_replace_io")
        self.gridLayout.addWidget(self.txt_replace_io, 7, 1, 1, 2)
        self.lbl_lbl_reset_driver_action = QtWidgets.QLabel(self.gb_plc)
        self.lbl_lbl_reset_driver_action.setObjectName("lbl_lbl_reset_driver_action")
        self.gridLayout.addWidget(self.lbl_lbl_reset_driver_action, 9, 0, 1, 3)
        self.verticalLayout.addWidget(self.gb_plc)
        self.gb_server = QtWidgets.QGroupBox(diag_options)
        self.gb_server.setObjectName("gb_server")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gb_server)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_aclplcslave = QtWidgets.QPushButton(self.gb_server)
        self.btn_aclplcslave.setObjectName("btn_aclplcslave")
        self.gridLayout_2.addWidget(self.btn_aclplcslave, 0, 1, 1, 1)
        self.cbx_mqtt = QtWidgets.QCheckBox(self.gb_server)
        self.cbx_mqtt.setObjectName("cbx_mqtt")
        self.gridLayout_2.addWidget(self.cbx_mqtt, 2, 0, 1, 1)
        self.cbx_plcslave = QtWidgets.QCheckBox(self.gb_server)
        self.cbx_plcslave.setObjectName("cbx_plcslave")
        self.gridLayout_2.addWidget(self.cbx_plcslave, 0, 0, 1, 1)
        self.lbl_slave_status = QtWidgets.QLabel(self.gb_server)
        self.lbl_slave_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_slave_status.setObjectName("lbl_slave_status")
        self.gridLayout_2.addWidget(self.lbl_slave_status, 1, 1, 1, 1)
        self.lbl_lbl_slave_status = QtWidgets.QLabel(self.gb_server)
        self.lbl_lbl_slave_status.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_lbl_slave_status.setObjectName("lbl_lbl_slave_status")
        self.gridLayout_2.addWidget(self.lbl_lbl_slave_status, 1, 0, 1, 1)
        self.lbl_mqtt_status = QtWidgets.QLabel(self.gb_server)
        self.lbl_mqtt_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_mqtt_status.setObjectName("lbl_mqtt_status")
        self.gridLayout_2.addWidget(self.lbl_mqtt_status, 3, 1, 1, 1)
        self.lbl_lbl_mqtt_status = QtWidgets.QLabel(self.gb_server)
        self.lbl_lbl_mqtt_status.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_lbl_mqtt_status.setObjectName("lbl_lbl_mqtt_status")
        self.gridLayout_2.addWidget(self.lbl_lbl_mqtt_status, 3, 0, 1, 1)
        self.btn_mqtt = QtWidgets.QPushButton(self.gb_server)
        self.btn_mqtt.setObjectName("btn_mqtt")
        self.gridLayout_2.addWidget(self.btn_mqtt, 2, 1, 1, 1)
        self.btn_aclxmlrpc = QtWidgets.QPushButton(self.gb_server)
        self.btn_aclxmlrpc.setObjectName("btn_aclxmlrpc")
        self.gridLayout_2.addWidget(self.btn_aclxmlrpc, 4, 1, 1, 1)
        self.cbx_xmlrpc = QtWidgets.QCheckBox(self.gb_server)
        self.cbx_xmlrpc.setObjectName("cbx_xmlrpc")
        self.gridLayout_2.addWidget(self.cbx_xmlrpc, 4, 0, 1, 1)
        self.verticalLayout.addWidget(self.gb_server)
        self.btn_box = QtWidgets.QDialogButtonBox(diag_options)
        self.btn_box.setOrientation(QtCore.Qt.Horizontal)
        self.btn_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_box.setObjectName("btn_box")
        self.verticalLayout.addWidget(self.btn_box)

        self.retranslateUi(diag_options)
        self.btn_box.accepted.connect(diag_options.accept)
        self.btn_box.rejected.connect(diag_options.reject)
        QtCore.QMetaObject.connectSlotsByName(diag_options)

    def retranslateUi(self, diag_options):
        _translate = QtCore.QCoreApplication.translate
        diag_options.setWindowTitle(_translate("diag_options", "RevPi Python PLC Options"))
        self.gb_plc.setTitle(_translate("diag_options", "Start / Stop behavior of PLC program"))
        self.lbl_replace_io.setText(_translate("diag_options", "Replace IO file:"))
        self.cbx_zeroonerror.setText(_translate("diag_options", "... after exception and errors"))
        self.cbx_autostart.setText(_translate("diag_options", "Start PLC program automatically"))
        self.cbb_reset_driver_action.setItemText(0, _translate("diag_options", "Do nothing"))
        self.cbb_reset_driver_action.setItemText(1, _translate("diag_options", "Restart after piCtory changed"))
        self.cbb_reset_driver_action.setItemText(2, _translate("diag_options", "Always restart the PLC program"))
        self.lbl_reset_driver_action.setText(_translate("diag_options", "Driver reset action:"))
        self.lbl_plc_zero.setText(_translate("diag_options", "Set process image to NULL if program terminates..."))
        self.cbb_replace_io.setItemText(0, _translate("diag_options", "Do not use replace io file"))
        self.cbb_replace_io.setItemText(1, _translate("diag_options", "Use static file from RevPiPyLoad"))
        self.cbb_replace_io.setItemText(2, _translate("diag_options", "Use dynamic file from work directory"))
        self.cbb_replace_io.setItemText(3, _translate("diag_options", "Give own path and filename"))
        self.cbx_zeroonexit.setText(_translate("diag_options", "... sucessfully without error"))
        self.lbl_plc_delay.setText(_translate("diag_options", "Restart delay in seconds:"))
        self.cbx_autoreload.setText(_translate("diag_options", "Restart PLC program after exit or crash"))
        self.lbl_lbl_reset_driver_action.setText(_translate("diag_options", "PLC program behavior after piCtory driver reset clicked"))
        self.gb_server.setTitle(_translate("diag_options", "RevPiPyLoad server services"))
        self.btn_aclplcslave.setText(_translate("diag_options", "Edit ACL"))
        self.cbx_mqtt.setText(_translate("diag_options", "MQTT process image publisher"))
        self.cbx_plcslave.setText(_translate("diag_options", "Start RevPi piControl server"))
        self.lbl_slave_status.setText(_translate("diag_options", "status"))
        self.lbl_lbl_slave_status.setText(_translate("diag_options", "piControl server is:"))
        self.lbl_mqtt_status.setText(_translate("diag_options", "status"))
        self.lbl_lbl_mqtt_status.setText(_translate("diag_options", "MQTT publish service is:"))
        self.btn_mqtt.setText(_translate("diag_options", "Settings"))
        self.btn_aclxmlrpc.setText(_translate("diag_options", "Edit ACL"))
        self.cbx_xmlrpc.setText(_translate("diag_options", "Activate XML-RPC for RevPiCommander"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    diag_options = QtWidgets.QDialog()
    ui = Ui_diag_options()
    ui.setupUi(diag_options)
    diag_options.show()
    sys.exit(app.exec_())
