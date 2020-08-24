# -*- coding: utf-8 -*-
"""Revolution Pi search with zeroconf."""
__author__ = "Sven Sager"
__copyright__ = "Copyright (C) 2020 Sven Sager"
__license__ = "GPLv3"

from os import name as osname
from re import compile
from socket import gethostbyname

from PyQt5 import QtCore, QtGui, QtWidgets
from zeroconf import ServiceBrowser, Zeroconf

import helper
import proginit as pi
from helper import WidgetData
from ui.avahisearch_ui import Ui_diag_search


class AvahiSearchThread(QtCore.QThread):
    """Search thread for Revolution Pi with installed RevPiPyLoad."""
    added = QtCore.pyqtSignal(str, str, int, str, str)
    removed = QtCore.pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(AvahiSearchThread, self).__init__(parent)
        self._cycle_wait_ms = 1000

        self.__dict_arp = {}
        self.re_posix = compile(
            r"(?P<ip>(\d{1,3}\.){3}\d{1,3}).*"
            r"(?P<mac>([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})"
        )

    def _update_arp(self):
        if osname == "posix":
            with open("/proc/net/arp") as fh:
                for line in fh.readlines():
                    ip_mac = self.re_posix.search(line)
                    if ip_mac:
                        self.__dict_arp[ip_mac.group("ip")] = ip_mac.group("mac")

    def get_mac(self, ip: str):
        return self.__dict_arp.get(ip, None)

    def remove_service(self, zeroconf: Zeroconf, conf_type: str, name: str):
        """Revolution Pi disappeared."""
        pi.logger.debug("AvahiSearchThread.remove_service")
        self.removed.emit(name, conf_type)

    def add_service(self, zeroconf: Zeroconf, conf_type: str, name: str):
        """New Revolution Pi found."""
        pi.logger.debug("AvahiSearchThread.add_service")
        info = zeroconf.get_service_info(conf_type, name)
        if not info:
            return

        try:
            ip = gethostbyname(info.server)
        except Exception:
            ip = self.tr("N/A")
        self.added.emit(name, info.server, info.port, conf_type, ip)

    def run(self):
        pi.logger.debug("Started zero conf discovery.")
        zeroconf = Zeroconf()
        revpi_browser = ServiceBrowser(zeroconf, "_revpipyload._tcp.local.", self)
        while not self.isInterruptionRequested():
            # Just hanging around :)
            self.msleep(self._cycle_wait_ms)
        zeroconf.close()
        pi.logger.debug("Stopped zero conf discovery.")


class AvahiSearch(QtWidgets.QDialog, Ui_diag_search):

    def __init__(self, parent=None):
        super(AvahiSearch, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.connect_index = -1
        self.th_zero_conf = AvahiSearchThread(self)

        self.tb_revpi.setColumnWidth(0, 250)
        self.btn_connect.setEnabled(False)
        self.btn_save.setEnabled(False)

    def _restart_search(self):
        """Clean up an restart search thread."""
        while self.tb_revpi.rowCount() > 0:
            self.tb_revpi.removeRow(0)
        self.th_zero_conf.requestInterruption()

        self.th_zero_conf = AvahiSearchThread(self)
        self.th_zero_conf.added.connect(self.on_avahi_added)
        self.th_zero_conf.removed.connect(self.on_avahi_removed)
        self.th_zero_conf.start()

    def _save_connection(self, row: int, no_warn=False):
        """
        Save the connection from given row to settings.

        :param row: Row with connection data
        :param no_warn: If True, no message boxes will appear
        :return: Array index of connection (found or saved)
        """
        item = self.tb_revpi.item(row, 0)
        if not item:
            return

        folder_name = self.tr("Auto discovered")
        selected_name = item.text()
        selected_address = item.data(WidgetData.address)
        selected_port = item.data(WidgetData.port)
        i = 0
        for i in range(helper.settings.beginReadArray("connections")):
            helper.settings.setArrayIndex(i)

            name = helper.settings.value("name", type=str)
            address = helper.settings.value("address", type=str)
            port = helper.settings.value("port", type=int)
            if address.lower() == selected_address.lower() and port == selected_port:
                if not no_warn:
                    QtWidgets.QMessageBox.information(
                        self, self.tr("Already in list..."), self.tr(
                            "The selected Revolution Pi is already saved in your "
                            "connection list as '{0}.".format(name)
                        )
                    )
                helper.settings.endArray()
                return i

        helper.settings.endArray()
        helper.settings.beginWriteArray("connections")

        helper.settings.setArrayIndex(i + 1)
        helper.settings.setValue("address", selected_address)
        helper.settings.setValue("folder", folder_name)
        helper.settings.setValue("name", selected_name)
        helper.settings.setValue("port", selected_port)

        helper.settings.endArray()

        if not no_warn:
            QtWidgets.QMessageBox.information(
                self, self.tr("Success"), self.tr(
                    "The connection with the name '{0}' was successfully saved "
                    "to folder '{1}' in your connections.".format(selected_name, folder_name)
                )
            )

        return i + 1

    def exec(self) -> int:
        self._restart_search()
        rc = super(AvahiSearch, self).exec()
        self.th_zero_conf.requestInterruption()
        return rc

    @QtCore.pyqtSlot(str, str, int, str, str)
    def on_avahi_added(self, name: str, server: str, port: int, conf_type: str, ip: str):
        """New Revolution Pi found."""
        index = -1
        for i in range(self.tb_revpi.rowCount()):
            if self.tb_revpi.item(i, 0).data(WidgetData.object_name) == name:
                index = i
                break

        if index == -1:
            # New Row
            item_name = QtWidgets.QTableWidgetItem()
            item_ip = QtWidgets.QTableWidgetItem()

            index = self.tb_revpi.rowCount()
            self.tb_revpi.insertRow(index)
            self.tb_revpi.setItem(index, 0, item_name)
            self.tb_revpi.setItem(index, 1, item_ip)
        else:
            # Update row
            item_name = self.tb_revpi.item(index, 0)
            item_ip = self.tb_revpi.item(index, 1)

        item_name.setIcon(QtGui.QIcon(":/main/ico/cpu.ico"))
        item_name.setText(server[:-1])
        item_name.setData(WidgetData.object_name, name)
        item_name.setData(WidgetData.address, server[:-1])
        item_name.setData(WidgetData.port, port)
        item_ip.setText(ip)

    @QtCore.pyqtSlot(str, str)
    def on_avahi_removed(self, name: str, conf_type: str):
        """Revolution Pi disappeared."""
        for i in range(self.tb_revpi.rowCount()):
            if self.tb_revpi.item(i, 0).data(WidgetData.object_name) == name:
                self.tb_revpi.removeRow(i)
                break

    @QtCore.pyqtSlot(int, int)
    def on_tb_revpi_cellDoubleClicked(self, row: int, column: int):
        """Connect to double clicked Revolution Pi."""
        pi.logger.debug("AvahiSearch.on_tb_revpi_cellDoubleClicked")
        self.connect_index = self._save_connection(row, no_warn=True)
        self.accept()

    @QtCore.pyqtSlot(int, int, int, int)
    def on_tb_revpi_currentCellChanged(self, row: int, column: int, last_row: int, last_column: int):
        """Manage state of buttons."""
        self.btn_connect.setEnabled(row >= 0)
        self.btn_save.setEnabled(row >= 0)

    @QtCore.pyqtSlot()
    def on_btn_connect_pressed(self):
        """Connect to selected Revolution Pi."""
        pi.logger.debug("AvahiSearch.on_btn_connect_pressed")
        if self.tb_revpi.currentRow() == -1:
            return
        self.connect_index = self._save_connection(self.tb_revpi.currentRow(), no_warn=True)
        self.accept()

    @QtCore.pyqtSlot()
    def on_btn_save_pressed(self):
        """Save selected Revolution Pi."""
        pi.logger.debug("AvahiSearch.on_btn_save_pressed")
        if self.tb_revpi.currentRow() == -1:
            return
        self.connect_index = self._save_connection(self.tb_revpi.currentRow())

    @QtCore.pyqtSlot()
    def on_btn_restart_pressed(self):
        """Clean up an restart search thread."""
        self._restart_search()
