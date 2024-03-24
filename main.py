from ui.main import Main
from PyQt5 import QtWidgets
from os import path, environ

script_dir = path.dirname(path.abspath(__file__))
print(script_dir)
environ['PATH_SCRIPT'] = script_dir
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main(MainWindow, app)
    MainWindow.show()
    sys.exit(app.exec_())
