# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'revpiprogram.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_diag_program(object):
    def setupUi(self, diag_program):
        diag_program.setObjectName("diag_program")
        diag_program.resize(488, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(diag_program)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gb_plc = QtWidgets.QGroupBox(diag_program)
        self.gb_plc.setObjectName("gb_plc")
        self.gridLayout = QtWidgets.QGridLayout(self.gb_plc)
        self.gridLayout.setObjectName("gridLayout")
        self.rbn_pythonversion_2 = QtWidgets.QRadioButton(self.gb_plc)
        self.rbn_pythonversion_2.setObjectName("rbn_pythonversion_2")
        self.gridLayout.addWidget(self.rbn_pythonversion_2, 3, 1, 1, 1)
        self.txt_plcarguments = QtWidgets.QLineEdit(self.gb_plc)
        self.txt_plcarguments.setObjectName("txt_plcarguments")
        self.gridLayout.addWidget(self.txt_plcarguments, 2, 1, 1, 2)
        self.rbn_pythonversion_3 = QtWidgets.QRadioButton(self.gb_plc)
        self.rbn_pythonversion_3.setObjectName("rbn_pythonversion_3")
        self.gridLayout.addWidget(self.rbn_pythonversion_3, 3, 2, 1, 1)
        self.lbl_plcprogram = QtWidgets.QLabel(self.gb_plc)
        self.lbl_plcprogram.setObjectName("lbl_plcprogram")
        self.gridLayout.addWidget(self.lbl_plcprogram, 0, 0, 1, 3)
        self.cbx_plcworkdir_set_uid = QtWidgets.QCheckBox(self.gb_plc)
        self.cbx_plcworkdir_set_uid.setObjectName("cbx_plcworkdir_set_uid")
        self.gridLayout.addWidget(self.cbx_plcworkdir_set_uid, 4, 0, 1, 3)
        self.cbb_plcprogram = QtWidgets.QComboBox(self.gb_plc)
        self.cbb_plcprogram.setObjectName("cbb_plcprogram")
        self.gridLayout.addWidget(self.cbb_plcprogram, 1, 0, 1, 3)
        self.lbl_pythonversion = QtWidgets.QLabel(self.gb_plc)
        self.lbl_pythonversion.setObjectName("lbl_pythonversion")
        self.gridLayout.addWidget(self.lbl_pythonversion, 3, 0, 1, 1)
        self.lbl_plcarguments = QtWidgets.QLabel(self.gb_plc)
        self.lbl_plcarguments.setObjectName("lbl_plcarguments")
        self.gridLayout.addWidget(self.lbl_plcarguments, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.gb_plc)
        self.cb_transfair = QtWidgets.QGroupBox(diag_program)
        self.cb_transfair.setObjectName("cb_transfair")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.cb_transfair)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cbb_format = QtWidgets.QComboBox(self.cb_transfair)
        self.cbb_format.setObjectName("cbb_format")
        self.cbb_format.addItem("")
        self.cbb_format.addItem("")
        self.cbb_format.addItem("")
        self.cbb_format.addItem("")
        self.gridLayout_2.addWidget(self.cbb_format, 0, 1, 1, 1)
        self.btn_program_upload = QtWidgets.QPushButton(self.cb_transfair)
        self.btn_program_upload.setObjectName("btn_program_upload")
        self.gridLayout_2.addWidget(self.btn_program_upload, 3, 1, 1, 1)
        self.btn_program_download = QtWidgets.QPushButton(self.cb_transfair)
        self.btn_program_download.setObjectName("btn_program_download")
        self.gridLayout_2.addWidget(self.btn_program_download, 3, 0, 1, 1)
        self.lbl_format = QtWidgets.QLabel(self.cb_transfair)
        self.lbl_format.setObjectName("lbl_format")
        self.gridLayout_2.addWidget(self.lbl_format, 0, 0, 1, 1)
        self.cbx_pictory = QtWidgets.QCheckBox(self.cb_transfair)
        self.cbx_pictory.setObjectName("cbx_pictory")
        self.gridLayout_2.addWidget(self.cbx_pictory, 1, 0, 1, 2)
        self.cbx_clear = QtWidgets.QCheckBox(self.cb_transfair)
        self.cbx_clear.setObjectName("cbx_clear")
        self.gridLayout_2.addWidget(self.cbx_clear, 2, 0, 1, 2)
        self.verticalLayout.addWidget(self.cb_transfair)
        self.gb_control = QtWidgets.QGroupBox(diag_program)
        self.gb_control.setObjectName("gb_control")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gb_control)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_procimg_download = QtWidgets.QPushButton(self.gb_control)
        self.btn_procimg_download.setObjectName("btn_procimg_download")
        self.gridLayout_3.addWidget(self.btn_procimg_download, 1, 1, 1, 1)
        self.btn_pictory_download = QtWidgets.QPushButton(self.gb_control)
        self.btn_pictory_download.setObjectName("btn_pictory_download")
        self.gridLayout_3.addWidget(self.btn_pictory_download, 0, 1, 1, 1)
        self.btn_pictory_upload = QtWidgets.QPushButton(self.gb_control)
        self.btn_pictory_upload.setObjectName("btn_pictory_upload")
        self.gridLayout_3.addWidget(self.btn_pictory_upload, 0, 2, 1, 1)
        self.lbl_pictory = QtWidgets.QLabel(self.gb_control)
        self.lbl_pictory.setObjectName("lbl_pictory")
        self.gridLayout_3.addWidget(self.lbl_pictory, 0, 0, 1, 1)
        self.lbl_procimg = QtWidgets.QLabel(self.gb_control)
        self.lbl_procimg.setObjectName("lbl_procimg")
        self.gridLayout_3.addWidget(self.lbl_procimg, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.gb_control)
        self.btn_box = QtWidgets.QDialogButtonBox(diag_program)
        self.btn_box.setOrientation(QtCore.Qt.Horizontal)
        self.btn_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_box.setObjectName("btn_box")
        self.verticalLayout.addWidget(self.btn_box)

        self.retranslateUi(diag_program)
        self.btn_box.accepted.connect(diag_program.accept)
        self.btn_box.rejected.connect(diag_program.reject)
        QtCore.QMetaObject.connectSlotsByName(diag_program)
        diag_program.setTabOrder(self.cbb_plcprogram, self.txt_plcarguments)
        diag_program.setTabOrder(self.txt_plcarguments, self.rbn_pythonversion_2)
        diag_program.setTabOrder(self.rbn_pythonversion_2, self.rbn_pythonversion_3)
        diag_program.setTabOrder(self.rbn_pythonversion_3, self.cbx_plcworkdir_set_uid)
        diag_program.setTabOrder(self.cbx_plcworkdir_set_uid, self.cbb_format)
        diag_program.setTabOrder(self.cbb_format, self.cbx_pictory)
        diag_program.setTabOrder(self.cbx_pictory, self.cbx_clear)
        diag_program.setTabOrder(self.cbx_clear, self.btn_program_download)
        diag_program.setTabOrder(self.btn_program_download, self.btn_program_upload)
        diag_program.setTabOrder(self.btn_program_upload, self.btn_pictory_download)
        diag_program.setTabOrder(self.btn_pictory_download, self.btn_pictory_upload)
        diag_program.setTabOrder(self.btn_pictory_upload, self.btn_procimg_download)

    def retranslateUi(self, diag_program):
        _translate = QtCore.QCoreApplication.translate
        diag_program.setWindowTitle(_translate("diag_program", "PLC program"))
        self.gb_plc.setTitle(_translate("diag_program", "PLC program"))
        self.rbn_pythonversion_2.setText(_translate("diag_program", "Python 2"))
        self.rbn_pythonversion_3.setText(_translate("diag_program", "Python 3"))
        self.lbl_plcprogram.setText(_translate("diag_program", "Python PLC start program:"))
        self.cbx_plcworkdir_set_uid.setText(_translate("diag_program", "Set write permissions for plc program to workdirectory"))
        self.lbl_pythonversion.setText(_translate("diag_program", "Python version:"))
        self.lbl_plcarguments.setText(_translate("diag_program", "Program arguments:"))
        self.cb_transfair.setTitle(_translate("diag_program", "Transfair PLC program"))
        self.cbb_format.setItemText(0, _translate("diag_program", "Files"))
        self.cbb_format.setItemText(1, _translate("diag_program", "Folder"))
        self.cbb_format.setItemText(2, _translate("diag_program", "ZIP archive"))
        self.cbb_format.setItemText(3, _translate("diag_program", "TGZ archive"))
        self.btn_program_upload.setText(_translate("diag_program", "Upload"))
        self.btn_program_download.setText(_translate("diag_program", "Download"))
        self.lbl_format.setText(_translate("diag_program", "Transfair format:"))
        self.cbx_pictory.setText(_translate("diag_program", "Including piCtory configuration"))
        self.cbx_clear.setText(_translate("diag_program", "Remove all files on Revolution Pi before upload"))
        self.gb_control.setTitle(_translate("diag_program", "Control files"))
        self.btn_procimg_download.setText(_translate("diag_program", "Download"))
        self.btn_pictory_download.setText(_translate("diag_program", "Download"))
        self.btn_pictory_upload.setText(_translate("diag_program", "Upload"))
        self.lbl_pictory.setText(_translate("diag_program", "piCtory configuraiton"))
        self.lbl_procimg.setText(_translate("diag_program", "Process image from piControl0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    diag_program = QtWidgets.QDialog()
    ui = Ui_diag_program()
    ui.setupUi(diag_program)
    diag_program.show()
    sys.exit(app.exec_())

