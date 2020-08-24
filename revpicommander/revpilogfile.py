# -*- coding: utf-8 -*-
"""View log files from Revolution Pi."""
__author__ = "Sven Sager"
__copyright__ = "Copyright (C) 2018 Sven Sager"
__license__ = "GPLv3"

from enum import IntEnum

from PyQt5 import QtCore, QtGui, QtWidgets

import helper
import proginit as pi
from ui.revpilogfile_ui import Ui_win_revpilogfile


class LogType(IntEnum):
    NONE = 0
    APP = 1
    DAEMON = 2


class DataThread(QtCore.QThread):

    error_detected = QtCore.pyqtSignal()
    line_logged = QtCore.pyqtSignal(LogType, bool, str)

    def __init__(self, parent=None, cycle_time=1000):
        super(DataThread, self).__init__(parent)

        self._cli = helper.cm.get_cli()
        self._cycle_time = cycle_time
        self._paused = True
        self.error_count = 0
        self.max_block = 16384
        self.mrk_app = 0
        self.mrk_daemon = 0

    def _load_log(self, log_type: LogType, xmlcall, start_position: int):
        """
        Get log text and put it to log viewer.

        :param log_type: Type of log file <class 'LogType'>
        :param xmlcall: XML-RPC call to get log text
        :param start_position: Start position in log file to read from
        :return: New position in log file
        """
        buff_log = b''
        while True:
            # Load max data from start position to see the end of logfile
            bytebuff = xmlcall(start_position, self.max_block).data
            buff_log += bytebuff
            start_position += len(bytebuff)

            # If we get less than max_block, the log file is EOF for this time
            if len(bytebuff) < self.max_block:
                break

        if bytebuff == b'\x16':  # 'ESC'
            # RevPiPyLoad could not access log file on Revolution Pi
            self.line_logged.emit(log_type, False, "")

        elif bytebuff == b'\x19':  # 'EndOfMedia'
            # The log file was rotated by log rotate on the Revolution Pi
            start_position = 0

        elif buff_log:
            self.line_logged.emit(log_type, True, buff_log.decode("utf-8"))

        return start_position

    def pause(self):
        """Stop checking new log lines, but leave thread alive."""
        self._paused = True

    def resume(self):
        """Start checking for new log lines."""
        self._paused = False

    def run(self) -> None:
        pi.logger.debug("DataThread.run")

        while not self.isInterruptionRequested():
            if not self._paused:
                try:
                    self.mrk_app = self._load_log(
                        LogType.APP,
                        self._cli.load_applog,
                        self.mrk_app,
                    )
                    self.mrk_daemon = self._load_log(
                        LogType.DAEMON,
                        self._cli.load_plclog,
                        self.mrk_daemon,
                    )
                    self.error_count = 0
                except Exception:
                    if self.error_count == 0:
                        self.error_detected.emit()
                    self.error_count += 1

            self.msleep(self._cycle_time)


class RevPiLogfile(QtWidgets.QMainWindow, Ui_win_revpilogfile):
    """Log file viewer for daemon and plc program log."""

    def __init__(self, parent):
        u"""Init RevPiLogfile-Class."""
        super(RevPiLogfile, self).__init__(parent)
        self.setupUi(self)

        self.th_data = DataThread()
        self.err_daemon = 0

        helper.cm.connection_established.connect(self.on_cm_connection_established)
        helper.cm.connection_disconnecting.connect(self.on_cm_connection_disconnecting)

        self._load_gui_settings()

    def __del__(self):
        pi.logger.debug("RevPiLogfile.__del__")
        self.th_data.deleteLater()

    def _create_data_thread(self):
        self.th_data.deleteLater()

        self.th_data = DataThread()
        self.th_data.line_logged.connect(self.on_line_logged)
        self.th_data.start()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        helper.settings.setValue("logfile/geo", self.saveGeometry())
        helper.settings.setValue("logfile/stay_on_top", self.cbx_stay_on_top.isChecked())

    def hideEvent(self, a0: QtGui.QHideEvent) -> None:
        self.th_data.pause()
        super(RevPiLogfile, self).hideEvent(a0)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.th_data.resume()
        super(RevPiLogfile, self).showEvent(a0)

    def _load_gui_settings(self):
        self.restoreGeometry(helper.settings.value("logfile/geo", b''))
        self.cbx_stay_on_top.setChecked(helper.settings.value("logfile/stay_on_top", False, bool))
        self.cbx_wrap.setChecked(helper.settings.value("logfile/wrap", False, bool))

    @QtCore.pyqtSlot()
    def on_cm_connection_disconnecting(self):
        """Disconnecting form Revolution Pi."""
        self.th_data.requestInterruption()
        self.th_data.wait()

    @QtCore.pyqtSlot()
    def on_cm_connection_established(self):
        """New connection established."""
        self.txt_app.clear()
        self.txt_daemon.clear()

        self._create_data_thread()
        if self.isVisible():
            self.th_data.resume()

    @QtCore.pyqtSlot()
    def on_btn_daemon_pressed(self):
        """Clear the daemon log view."""
        self.txt_daemon.clear()

    @QtCore.pyqtSlot()
    def on_btn_app_pressed(self):
        """Clear the app log view."""
        self.txt_app.clear()

    @QtCore.pyqtSlot(int)
    def on_cbx_stay_on_top_stateChanged(self, state: int):
        """Set flag to stay on top of all windows."""
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, state == QtCore.Qt.Checked)

    @QtCore.pyqtSlot(int)
    def on_cbx_wrap_stateChanged(self, state: int):
        """Line wrap mode."""
        wrap_mode = QtWidgets.QPlainTextEdit.WidgetWidth if state == QtCore.Qt.Checked else \
            QtWidgets.QPlainTextEdit.NoWrap
        self.txt_daemon.setLineWrapMode(wrap_mode)
        self.txt_app.setLineWrapMode(wrap_mode)
        helper.settings.setValue("logfile/wrap", self.cbx_wrap.isChecked())

    @QtCore.pyqtSlot(LogType, bool, str)
    def on_line_logged(self, log_type: LogType, success: bool, text: str):
        pi.logger.debug("RevPiLogfile.on_line_logged")

        if log_type == LogType.APP:
            textwidget = self.txt_app
        elif log_type == LogType.DAEMON:
            textwidget = self.txt_daemon
        else:
            return

        bar = textwidget.verticalScrollBar()
        auto_scroll = bar.value() == bar.maximum()

        if not success:
            textwidget.clear()
            textwidget.setPlainText(self.tr("Can not access log file on the RevPi"))
        elif text != "":
            # Function will add \n automatically
            textwidget.appendPlainText(text.strip("\n"))
            if auto_scroll:
                bar.setValue(bar.maximum())
