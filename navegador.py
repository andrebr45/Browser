#IMPORTAR 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import * 
import sys

class MainWindows(QMainWindow):
    def __init__(self,*args, **kwargs) -> None:
        super(MainWindows, self).__init__(*args, **kwargs)

        self.showMaximized()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        self.setCentralWidget(self.browser)
        self.show()

app = QApplication(sys.argv)
window = MainWindows()

app.exec_()