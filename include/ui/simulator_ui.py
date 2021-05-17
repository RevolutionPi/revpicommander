# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulator.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_diag_simulator(object):
    def setupUi(self, diag_simulator):
        diag_simulator.setObjectName("diag_simulator")
        diag_simulator.resize(522, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(diag_simulator)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gb_settings = QtWidgets.QGroupBox(diag_simulator)
        self.gb_settings.setObjectName("gb_settings")
        self.gridLayout = QtWidgets.QGridLayout(self.gb_settings)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_history = QtWidgets.QLabel(self.gb_settings)
        self.lbl_history.setObjectName("lbl_history")
        self.gridLayout.addWidget(self.lbl_history, 0, 0, 1, 1)
        self.lbl_configrsc = QtWidgets.QLabel(self.gb_settings)
        self.lbl_configrsc.setObjectName("lbl_configrsc")
        self.gridLayout.addWidget(self.lbl_configrsc, 1, 0, 1, 1)
        self.txt_configrsc = QtWidgets.QLineEdit(self.gb_settings)
        self.txt_configrsc.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txt_configrsc.setText("")
        self.txt_configrsc.setObjectName("txt_configrsc")
        self.gridLayout.addWidget(self.txt_configrsc, 1, 1, 1, 1)
        self.btn_configrsc = QtWidgets.QPushButton(self.gb_settings)
        self.btn_configrsc.setObjectName("btn_configrsc")
        self.gridLayout.addWidget(self.btn_configrsc, 1, 2, 1, 1)
        self.lbl_procimg = QtWidgets.QLabel(self.gb_settings)
        self.lbl_procimg.setObjectName("lbl_procimg")
        self.gridLayout.addWidget(self.lbl_procimg, 2, 0, 1, 1)
        self.txt_procimg = QtWidgets.QLineEdit(self.gb_settings)
        self.txt_procimg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txt_procimg.setText("")
        self.txt_procimg.setObjectName("txt_procimg")
        self.gridLayout.addWidget(self.txt_procimg, 2, 1, 1, 1)
        self.lbl_stop = QtWidgets.QLabel(self.gb_settings)
        self.lbl_stop.setObjectName("lbl_stop")
        self.gridLayout.addWidget(self.lbl_stop, 3, 0, 1, 1)
        self.lbl_restart = QtWidgets.QLabel(self.gb_settings)
        self.lbl_restart.setObjectName("lbl_restart")
        self.gridLayout.addWidget(self.lbl_restart, 4, 0, 1, 1)
        self.cbb_history = QtWidgets.QComboBox(self.gb_settings)
        self.cbb_history.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cbb_history.setObjectName("cbb_history")
        self.gridLayout.addWidget(self.cbb_history, 0, 1, 1, 2)
        self.cbx_stop_remove = QtWidgets.QCheckBox(self.gb_settings)
        self.cbx_stop_remove.setObjectName("cbx_stop_remove")
        self.gridLayout.addWidget(self.cbx_stop_remove, 3, 1, 1, 2)
        self.rb_restart_pictory = QtWidgets.QRadioButton(self.gb_settings)
        self.rb_restart_pictory.setChecked(True)
        self.rb_restart_pictory.setObjectName("rb_restart_pictory")
        self.gridLayout.addWidget(self.rb_restart_pictory, 4, 1, 1, 2)
        self.rb_restart_zero = QtWidgets.QRadioButton(self.gb_settings)
        self.rb_restart_zero.setObjectName("rb_restart_zero")
        self.gridLayout.addWidget(self.rb_restart_zero, 5, 1, 1, 2)
        self.verticalLayout.addWidget(self.gb_settings)
        self.gb_info = QtWidgets.QGroupBox(diag_simulator)
        self.gb_info.setObjectName("gb_info")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gb_info)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_info = QtWidgets.QLabel(self.gb_info)
        self.lbl_info.setWordWrap(True)
        self.lbl_info.setObjectName("lbl_info")
        self.verticalLayout_2.addWidget(self.lbl_info)
        self.txt_info = QtWidgets.QPlainTextEdit(self.gb_info)
        self.txt_info.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.txt_info.setReadOnly(True)
        self.txt_info.setPlainText("")
        self.txt_info.setObjectName("txt_info")
        self.verticalLayout_2.addWidget(self.txt_info)
        self.verticalLayout.addWidget(self.gb_info)
        self.btn_start_pictory = QtWidgets.QPushButton(diag_simulator)
        self.btn_start_pictory.setShortcut("Ctrl+1")
        self.btn_start_pictory.setObjectName("btn_start_pictory")
        self.verticalLayout.addWidget(self.btn_start_pictory)
        self.btn_start_empty = QtWidgets.QPushButton(diag_simulator)
        self.btn_start_empty.setShortcut("Ctrl+2")
        self.btn_start_empty.setObjectName("btn_start_empty")
        self.verticalLayout.addWidget(self.btn_start_empty)
        self.btn_start_nochange = QtWidgets.QPushButton(diag_simulator)
        self.btn_start_nochange.setShortcut("Ctrl+3")
        self.btn_start_nochange.setObjectName("btn_start_nochange")
        self.verticalLayout.addWidget(self.btn_start_nochange)

        self.retranslateUi(diag_simulator)
        self.btn_start_empty.clicked.connect(diag_simulator.accept)
        self.btn_start_nochange.clicked.connect(diag_simulator.accept)
        self.btn_start_pictory.clicked.connect(diag_simulator.accept)
        QtCore.QMetaObject.connectSlotsByName(diag_simulator)
        diag_simulator.setTabOrder(self.cbb_history, self.btn_configrsc)
        diag_simulator.setTabOrder(self.btn_configrsc, self.cbx_stop_remove)
        diag_simulator.setTabOrder(self.cbx_stop_remove, self.rb_restart_pictory)
        diag_simulator.setTabOrder(self.rb_restart_pictory, self.rb_restart_zero)
        diag_simulator.setTabOrder(self.rb_restart_zero, self.txt_info)
        diag_simulator.setTabOrder(self.txt_info, self.btn_start_pictory)
        diag_simulator.setTabOrder(self.btn_start_pictory, self.btn_start_empty)
        diag_simulator.setTabOrder(self.btn_start_empty, self.btn_start_nochange)

    def retranslateUi(self, diag_simulator):
        _translate = QtCore.QCoreApplication.translate
        diag_simulator.setWindowTitle(_translate("diag_simulator", "piControl simulator"))
        self.gb_settings.setTitle(_translate("diag_simulator", "Simulator settings"))
        self.lbl_history.setText(_translate("diag_simulator", "Last used:"))
        self.lbl_configrsc.setText(_translate("diag_simulator", "piCtory file:"))
        self.btn_configrsc.setText(_translate("diag_simulator", "select..."))
        self.lbl_procimg.setText(_translate("diag_simulator", "Process image:"))
        self.lbl_stop.setText(_translate("diag_simulator", "Stop action:"))
        self.lbl_restart.setText(_translate("diag_simulator", "Restart action:"))
        self.cbx_stop_remove.setText(_translate("diag_simulator", "Remove process image file"))
        self.rb_restart_pictory.setText(_translate("diag_simulator", "Restore piCtory default values"))
        self.rb_restart_zero.setText(_translate("diag_simulator", "Reset everything to ZERO"))
        self.gb_info.setTitle(_translate("diag_simulator", "RevPiModIO integration"))
        self.lbl_info.setText(_translate("diag_simulator", "You can work with this simulator if you call RevPiModIO with this additional parameters:"))
        self.btn_start_pictory.setText(_translate("diag_simulator", "Start with piCtory default values"))
        self.btn_start_empty.setText(_translate("diag_simulator", "Start with empty process image"))
        self.btn_start_nochange.setText(_translate("diag_simulator", "Start without changing actual process image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    diag_simulator = QtWidgets.QDialog()
    ui = Ui_diag_simulator()
    ui.setupUi(diag_simulator)
    diag_simulator.show()
    sys.exit(app.exec_())
