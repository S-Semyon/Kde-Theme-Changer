from ._ui_main import Ui_MainWindow
from modules.tools import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox, QDialog, QVBoxLayout, QLabel, QPushButton, QDialogButtonBox, QLineEdit, QInputDialog, QFileDialog
from PyQt5.QtCore import Qt, QTimer, QThread, QObject, pyqtSignal, QPoint
from PyQt5 import QtGui, QtCore
from modules import theme as kde_theme
from modules import tar
from shutil import ReadError
from tarfile import ReadError as tf_ReadError
import re, time, os

class Main(Ui_MainWindow):
    def __init__(self, MainWindow: QMainWindow, Application: QApplication):
        super().__init__(MainWindow)
        
        self.MainWindow = MainWindow
        self.Application = Application
        self.btn_new_theme.clicked.connect(self.new_theme)
        self.btn_remove_theme.clicked.connect(self.delete_theme)
        self.btn_accept.clicked.connect(self.accept_theme)
        self.btn_import.clicked.connect(self.import_theme)
        self.btn_export.clicked.connect(self.export_theme)
        self.list_themes.itemSelectionChanged.connect(self.on_item_selection_changed)
        #################################
        self.themes: dict[str, kde_theme.theme_data] = {}
        for theme in kde_theme.list_themes():
            if not isinstance(theme, kde_theme.theme_data):
                continue
            self.themes[theme.name] = theme
            self.list_themes.addItem(theme.name)

    @waiting_dialog(text="Через 5 секунд будет сделан скриншот экрана. \nСверните все приложения.", return_dialog = True)
    def _new_theme(self, theme_name: str, dialog: WaitingDialog | None = None):
        self.MainWindow.showMinimized()
        time.sleep(5)
        if dialog:
            dialog.showMinimized()
        kde_theme.save_theme(theme_name)
        time.sleep(1)
        if dialog:
            dialog.label.setText("Тема сохраняется")
            dialog.showNormal()
        time.sleep(10)
        
        
    @waiting_dialog(return_dialog=True)
    def _accept_theme(self, theme_name: str, dialog: WaitingDialog | None = None):
        kde_theme.load_theme(theme_name)
        if dialog:
            dialog.label.setText("По окончанию стоит перезагрузить пк")
        time.sleep(10)
    
    @waiting_dialog()
    def _del_theme(self, theme_name: str):
        kde_theme.del_theme(theme_name)

    def new_theme(self):
        """Создание новой темы"""
        input_dialog = QInputDialog(self.MainWindow, Qt.WindowCloseButtonHint) # type: ignore
        input_dialog.setStyleSheet("color: #fff;")
        input_dialog.setWindowTitle('Создание темы')
        input_dialog.setLabelText('Введите название темы:')
        input_dialog.exec_()
        new_theme = input_dialog.textValue()
        if not input_dialog.result():
            return
        if not re.match(r'^[a-zA-Zа-яА-Я0-9\s]+$', new_theme):
            error_box = QMessageBox()
            error_box.setWindowTitle("Ошибка")
            error_box.setWindowIcon(self.main_icon)
            error_box.setText(f"Название темы не должно включать в себя спецсимволы, либо оставаться пустым!")
            error_box.setIcon(QMessageBox.Warning)
            error_box.exec()
        elif self.list_themes.findItems(new_theme, Qt.MatchExactly): # type: ignore
            error_box = QMessageBox()
            error_box.setWindowTitle("Ошибка")
            error_box.setWindowIcon(self.main_icon)
            error_box.setText(f"Тема '{new_theme}' уже существует в списке!")
            error_box.setIcon(QMessageBox.Warning)
            error_box.exec()
        else:
            self._new_theme(new_theme)
            self.list_themes.addItem(new_theme)
            
    def delete_theme(self):
        """Удаление темы"""
        selected_items = self.list_themes.selectedItems()

        if not selected_items:
            return
        
        for item in selected_items:
            self._del_theme(item.text())
            self.list_themes.takeItem(self.list_themes.row(item))

    def accept_theme(self):
        selected = self.list_themes.selectedItems()
        if not selected:
            return
        self._accept_theme(selected[0].text())

    def export_theme(self):
        selected_items = self.list_themes.selectedItems()
        if not selected_items:
            return
        item = selected_items[0].text()
        theme_data = kde_theme.get_theme(item)
        if not theme_data:
            return 
        file_path, a = QFileDialog.getSaveFileName(
            self.MainWindow, 
            'Сохранить тему', 
            os.path.expanduser("~"),
            'Tar архив (*.tar)',
            )
        if not file_path:
            return
        tar.pack(file_path[:-4], theme_data.path)

    def import_theme(self):
        dialog = QFileDialog(directory=os.path.expanduser("~"))
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Tar архив (*.tar)")
        if dialog.exec_() != QFileDialog.Accepted:
            return
        filename = dialog.selectedFiles()[0]
        name = os.path.splitext(os.path.basename(filename))[0]
        save_path = kde_theme.SAVE_PATH + "/" + name
        try:
            filexist = tar.file_exist(filename, "screenshot.png")
        except tf_ReadError:
            error_box = QMessageBox()
            error_box.setWindowTitle("Ошибка")
            error_box.setWindowIcon(self.main_icon)
            error_box.setText(f"Архив битый")
            error_box.setIcon(QMessageBox.Warning)
            error_box.exec()
            return
        if not filexist:
            error_box = QMessageBox()
            error_box.setWindowTitle("Ошибка")
            error_box.setWindowIcon(self.main_icon)
            error_box.setText(f"В данном архиве нет темы")
            error_box.setIcon(QMessageBox.Warning)
            error_box.exec()
            return
        if kde_theme.get_theme(name):
            kde_theme.del_theme(name)
        try:
            tar.unpack(filename, save_path)
        except ReadError:
            error_box = QMessageBox()
            error_box.setWindowTitle("Ошибка")
            error_box.setWindowIcon(self.main_icon)
            error_box.setText(f"Архив битый")
            error_box.setIcon(QMessageBox.Warning)
            error_box.exec()
            return
        self.list_themes.addItem(name)

    def on_item_selection_changed(self):
        selected = self.list_themes.currentItem()
        if not selected:
            return
        theme = kde_theme.get_theme(selected.text())
        _translate = QtCore.QCoreApplication.translate
        self.img.setPixmap(QtGui.QPixmap(theme.path_to_img)) # type: ignore
        self.name_theme.setText(_translate("MainWindow", theme.name)) # type: ignore
