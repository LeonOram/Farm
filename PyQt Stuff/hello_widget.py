from PyQt4.QtGui import *
from PyQt4.QtCore import *

class HelloWidget(QWidget):
    Back = pyqtSignal()
    
    def __init__(self):
        super().__init__()

        self.label = QLabel("Hello")
        self.submit = QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.submit)

        self.setLayout(self.layout)

        self.submit.clicked.connect(self.submit_pushed)

    def submit_pushed(self):
        self.Back.emit()
