# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'revpiplclist.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_diag_connections(object):
    def setupUi(self, diag_connections):
        diag_connections.setObjectName("diag_connections")
        diag_connections.resize(496, 569)
        self.gridLayout = QtWidgets.QGridLayout(diag_connections)
        self.gridLayout.setObjectName("gridLayout")
        self.tab_properties = QtWidgets.QTabWidget(diag_connections)
        self.tab_properties.setObjectName("tab_properties")
        self.tab_connection = QtWidgets.QWidget()
        self.tab_connection.setObjectName("tab_connection")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tab_connection)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lbl_name = QtWidgets.QLabel(self.tab_connection)
        self.lbl_name.setObjectName("lbl_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_name)
        self.txt_name = QtWidgets.QLineEdit(self.tab_connection)
        self.txt_name.setObjectName("txt_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_name)
        self.lbl_address = QtWidgets.QLabel(self.tab_connection)
        self.lbl_address.setObjectName("lbl_address")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_address)
        self.txt_address = QtWidgets.QLineEdit(self.tab_connection)
        self.txt_address.setObjectName("txt_address")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_address)
        self.lbl_port = QtWidgets.QLabel(self.tab_connection)
        self.lbl_port.setObjectName("lbl_port")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_port)
        self.sbx_port = QtWidgets.QSpinBox(self.tab_connection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbx_port.sizePolicy().hasHeightForWidth())
        self.sbx_port.setSizePolicy(sizePolicy)
        self.sbx_port.setMinimum(1)
        self.sbx_port.setMaximum(65535)
        self.sbx_port.setProperty("value", 55123)
        self.sbx_port.setObjectName("sbx_port")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sbx_port)
        self.lbl_timeout = QtWidgets.QLabel(self.tab_connection)
        self.lbl_timeout.setObjectName("lbl_timeout")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_timeout)
        self.sbx_timeout = QtWidgets.QSpinBox(self.tab_connection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbx_timeout.sizePolicy().hasHeightForWidth())
        self.sbx_timeout.setSizePolicy(sizePolicy)
        self.sbx_timeout.setMinimum(5)
        self.sbx_timeout.setMaximum(30)
        self.sbx_timeout.setObjectName("sbx_timeout")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sbx_timeout)
        self.lbl_folder = QtWidgets.QLabel(self.tab_connection)
        self.lbl_folder.setObjectName("lbl_folder")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_folder)
        self.cbb_folder = QtWidgets.QComboBox(self.tab_connection)
        self.cbb_folder.setEditable(True)
        self.cbb_folder.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cbb_folder.setObjectName("cbb_folder")
        self.cbb_folder.addItem("")
        self.cbb_folder.setItemText(0, "")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cbb_folder)
        self.tab_properties.addTab(self.tab_connection, "")
        self.tab_ssh = QtWidgets.QWidget()
        self.tab_ssh.setObjectName("tab_ssh")
        self.formLayout = QtWidgets.QFormLayout(self.tab_ssh)
        self.formLayout.setObjectName("formLayout")
        self.lbl_ssh_use_tunnel = QtWidgets.QLabel(self.tab_ssh)
        self.lbl_ssh_use_tunnel.setObjectName("lbl_ssh_use_tunnel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_ssh_use_tunnel)
        self.cbx_ssh_use_tunnel = QtWidgets.QCheckBox(self.tab_ssh)
        self.cbx_ssh_use_tunnel.setText("")
        self.cbx_ssh_use_tunnel.setChecked(True)
        self.cbx_ssh_use_tunnel.setObjectName("cbx_ssh_use_tunnel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cbx_ssh_use_tunnel)
        self.lbl_ssh_port = QtWidgets.QLabel(self.tab_ssh)
        self.lbl_ssh_port.setObjectName("lbl_ssh_port")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_ssh_port)
        self.sbx_ssh_port = QtWidgets.QSpinBox(self.tab_ssh)
        self.sbx_ssh_port.setMaximum(65535)
        self.sbx_ssh_port.setProperty("value", 22)
        self.sbx_ssh_port.setObjectName("sbx_ssh_port")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sbx_ssh_port)
        self.lbl_ssh_user = QtWidgets.QLabel(self.tab_ssh)
        self.lbl_ssh_user.setObjectName("lbl_ssh_user")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_ssh_user)
        self.txt_ssh_user = QtWidgets.QLineEdit(self.tab_ssh)
        self.txt_ssh_user.setText("pi")
        self.txt_ssh_user.setObjectName("txt_ssh_user")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_ssh_user)
        self.tab_properties.addTab(self.tab_ssh, "")
        self.gridLayout.addWidget(self.tab_properties, 1, 0, 1, 2)
        self.btn_box = QtWidgets.QDialogButtonBox(diag_connections)
        self.btn_box.setOrientation(QtCore.Qt.Horizontal)
        self.btn_box.setStandardButtons(QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Save)
        self.btn_box.setObjectName("btn_box")
        self.gridLayout.addWidget(self.btn_box, 2, 0, 1, 2)
        self.tre_connections = QtWidgets.QTreeWidget(diag_connections)
        self.tre_connections.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tre_connections.setObjectName("tre_connections")
        self.gridLayout.addWidget(self.tre_connections, 0, 0, 1, 1)
        self.vl_edit = QtWidgets.QVBoxLayout()
        self.vl_edit.setObjectName("vl_edit")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vl_edit.addItem(spacerItem)
        self.btn_up = QtWidgets.QPushButton(diag_connections)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/action/ico/arrow-up.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_up.setIcon(icon)
        self.btn_up.setObjectName("btn_up")
        self.vl_edit.addWidget(self.btn_up)
        self.btn_down = QtWidgets.QPushButton(diag_connections)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/action/ico/arrow-down.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_down.setIcon(icon1)
        self.btn_down.setObjectName("btn_down")
        self.vl_edit.addWidget(self.btn_down)
        self.btn_delete = QtWidgets.QPushButton(diag_connections)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/action/ico/edit-delete-6.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon2)
        self.btn_delete.setObjectName("btn_delete")
        self.vl_edit.addWidget(self.btn_delete)
        self.btn_add_dir = QtWidgets.QPushButton(diag_connections)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/action/ico/folder-open.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_dir.setIcon(icon3)
        self.btn_add_dir.setObjectName("btn_add_dir")
        self.vl_edit.addWidget(self.btn_add_dir)
        self.btn_add = QtWidgets.QPushButton(diag_connections)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/action/ico/edit-add.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add.setIcon(icon4)
        self.btn_add.setObjectName("btn_add")
        self.vl_edit.addWidget(self.btn_add)
        self.gridLayout.addLayout(self.vl_edit, 0, 1, 1, 1)

        self.retranslateUi(diag_connections)
        self.tab_properties.setCurrentIndex(0)
        self.btn_box.rejected.connect(diag_connections.reject) # type: ignore
        self.btn_box.accepted.connect(diag_connections.accept) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(diag_connections)

    def retranslateUi(self, diag_connections):
        _translate = QtCore.QCoreApplication.translate
        diag_connections.setWindowTitle(_translate("diag_connections", "Revolution Pi connections"))
        self.lbl_name.setText(_translate("diag_connections", "Display name:"))
        self.lbl_address.setText(_translate("diag_connections", "Address (DNS/IP):"))
        self.lbl_port.setText(_translate("diag_connections", "Port (Default {0}):"))
        self.lbl_timeout.setText(_translate("diag_connections", "Connection timeout:"))
        self.sbx_timeout.setSuffix(_translate("diag_connections", " sec."))
        self.lbl_folder.setText(_translate("diag_connections", "Sub folder:"))
        self.tab_properties.setTabText(self.tab_properties.indexOf(self.tab_connection), _translate("diag_connections", "Connection"))
        self.lbl_ssh_use_tunnel.setText(_translate("diag_connections", "Connect over SSH tunnel:"))
        self.lbl_ssh_port.setText(_translate("diag_connections", "SSH port:"))
        self.lbl_ssh_user.setText(_translate("diag_connections", "SSH user name:"))
        self.tab_properties.setTabText(self.tab_properties.indexOf(self.tab_ssh), _translate("diag_connections", "Over SSH"))
        self.tre_connections.headerItem().setText(0, _translate("diag_connections", "Connection name"))
        self.tre_connections.headerItem().setText(1, _translate("diag_connections", "Address"))
from . import ressources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    diag_connections = QtWidgets.QDialog()
    ui = Ui_diag_connections()
    ui.setupUi(diag_connections)
    diag_connections.show()
    sys.exit(app.exec_())