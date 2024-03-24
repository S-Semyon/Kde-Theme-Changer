from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 518)
        MainWindow.setMinimumSize(QtCore.QSize(888, 518))
        MainWindow.setMaximumSize(QtCore.QSize(888, 518))
        self.main_icon = QtGui.QIcon()
        self.main_icon.addPixmap(QtGui.QPixmap("icons\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) # type: ignore
        MainWindow.setWindowIcon(self.main_icon)
        MainWindow.setStyleSheet("* {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background-color: #383838;\n"
"}\n"
"\n"
"QListWidget {\n"
"    border: 1px solid #000;\n"
"    background-color: #303030;\n"
"}\n"
"\n"
"#btn_new_theme," 
"#btn_import,\n"
"#btn_export,\n"
"#btn_accept,\n"
"#btn_remove_theme {\n"
"    background-color: #04AA6D;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"#btn_new_theme:hover,\n"
"#btn_import:hover,\n"
"#btn_export:hover,\n"
"#btn_accept:hover,\n"
"#btn_remove_theme:hover {\n"
"    background-color: #04915e;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name_theme = QtWidgets.QLabel(self.centralwidget)
        self.name_theme.setGeometry(QtCore.QRect(120, 20, 401, 51))
        self.name_theme.setStyleSheet("font: 22pt \"Segoe UI\";")
        self.name_theme.setAlignment(QtCore.Qt.AlignCenter) # type: ignore
        self.name_theme.setObjectName("name_theme")
        self.list_themes = QtWidgets.QListWidget(self.centralwidget)
        self.list_themes.setGeometry(QtCore.QRect(670, 90, 191, 341))
        self.list_themes.setObjectName("list_themes")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(650, 20, 221, 51))
        self.label_2.setStyleSheet("font: 22pt \"Segoe UI\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter) # type: ignore
        self.label_2.setObjectName("label_2")
        self.btn_accept = QtWidgets.QPushButton(self.centralwidget)
        self.btn_accept.setGeometry(QtCore.QRect(490, 460, 141, 41))
        self.btn_accept.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) # type: ignore
        self.btn_accept.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.btn_accept.setObjectName("btn_accept")
        self.btn_remove_theme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_remove_theme.setGeometry(QtCore.QRect(695, 460, 141, 41))
        self.btn_remove_theme.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) # type: ignore
        self.btn_remove_theme.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.btn_remove_theme.setObjectName("btn_remove_theme")
        self.btn_new_theme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_new_theme.setGeometry(QtCore.QRect(40, 460, 141, 41))
        self.btn_new_theme.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) # type: ignore
        self.btn_new_theme.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.btn_new_theme.setObjectName("btn_new_theme")
        self.btn_import = QtWidgets.QPushButton(self.centralwidget)
        self.btn_import.setGeometry(QtCore.QRect(190, 460, 141, 41))
        self.btn_import.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) # type: ignore
        self.btn_import.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.btn_import.setObjectName("btn_import")
        self.btn_export = QtWidgets.QPushButton(self.centralwidget)
        self.btn_export.setGeometry(QtCore.QRect(340, 460, 141, 41))
        self.btn_export.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) # type: ignore
        self.btn_export.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.btn_export.setObjectName("btn_export")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(40, 90, 561, 341))
        self.img.setPixmap(QtGui.QPixmap(r"C:\Users\Admin\Pictures\Screenshots\Снимок экрана (1).png"))
        self.img.setScaledContents(True)
        self.img.setAlignment(QtCore.Qt.AlignCenter) # type: ignore
        self.img.setObjectName("img")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KDE - Смена темы"))
        self.name_theme.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", "Список тем"))
        self.btn_accept.setText(_translate("MainWindow", "Применить"))
        self.btn_remove_theme.setText(_translate("MainWindow", "Удалить тему"))
        self.btn_new_theme.setText(_translate("MainWindow", "Новая тема"))
        self.btn_import.setText(_translate("MainWindow", "Импорт"))
        self.btn_export.setText(_translate("MainWindow", "Экспорт"))
