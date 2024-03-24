from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox, QDialog, QVBoxLayout, QLabel, QPushButton, QDialogButtonBox, QLineEdit
from PyQt5.QtCore import Qt, QTimer, QThread, QObject, pyqtSignal
from PyQt5 import QtGui
from modules import theme as kde_theme
import re

class WaitingDialog(QDialog):
    def __init__(self, text) -> None:
        super().__init__()
        self.setFixedSize(350, 60)
        self.setModal(True)
        self.setWindowFlags(Qt.FramelessWindowHint) # type: ignore
        layout = QVBoxLayout(self)
        self.label = QLabel(text)
        layout.addWidget(self.label)
        self.setWindowIcon(QtGui.QIcon("icons/logo.png"))

    def closeEvent(self, event):
        event.ignore()

def waiting_dialog(text: str = "", visible: bool = True, return_dialog: bool = False):
    def dec(func):
        def wrapper(cls, *args, **kwargs):

            waiting_dialog = WaitingDialog("Пожалуйста, подождите..." if not text else text)
            waiting_dialog.setStyleSheet("color: #fff;")
            waiting_dialog.show()

            class Worker(QObject):
                finished = pyqtSignal()
                def run(self):
                    if return_dialog:
                        func(cls, *args, **kwargs, dialog = waiting_dialog)
                    else:
                        func(cls, *args, **kwargs)
                    self.finished.emit()

            if not visible:
                waiting_dialog.showMinimized()
            th = QThread()
            w = Worker()
            w.moveToThread(th)
            th.started.connect( w.run )
            w.finished.connect(th.quit)
            th.start()
            th.finished.connect(waiting_dialog.accept)
            waiting_dialog.exec_()
        return wrapper
    return dec
