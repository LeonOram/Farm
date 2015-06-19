from PyQt4.QtGui import *
from PyQt4.QtCore import *

class NameWidget(QWidget):
    NameEntered = pyqtSignal()
    
    def __init__(self):
        super().__init__()

        self.username = QLineEdit()
        self.label = QLabel("Please enter name")
        self.submit = QPushButton("Submit")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.username)
        self.layout.addWidget(self.submit)

        self.setLayout(self.layout)

        self.submit.clicked.connect(self.submit_pushed)

    def submit_pushed(self):
        name = self.username.text()
        self.NameEntered.emit()
