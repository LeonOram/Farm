from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from name_widget import *
from hello_widget import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.name_widget = NameWidget()
        self.hello_widget = HelloWidget()
        self.stack = QStackedLayout()
        self.stack.addWidget(self.name_widget)
        self.stack.addWidget(self.hello_widget)
        self.widget = QWidget()
        self.widget.setLayout(self.stack)
        self.setCentralWidget(self.widget)

        self.name_widget.NameEntered.connect(self.name_provided)
        self.hello_widget.Back.connect(self.back_provided)

    def name_provided(self):
        self.stack.setCurrentIndex(1)
        name = self.name_widget.username.text()
        self.hello_widget.label.setText("Hello " + name)
        

    def back_provided(self):
        self.stack.setCurrentIndex(0)
        self.name_widget.username.clear()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.raise_()
    app.exec_()
