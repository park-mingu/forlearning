import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 400, 230, 450)

        # Label
        label = QLabel("층수", self)
        label.move(20, 20)

        label1 = QLabel("룸형태", self)
        label1.move(20, 60)

        label2 = QLabel("크기", self)
        label2.move(20, 100)

        label3 = QLabel("주방구조", self)
        label3.move(20, 140)

        label4 = QLabel("보증금", self)
        label4.move(20, 180)

        label5 = QLabel("월세", self)
        label5.move(20, 220)

        label6 = QLabel("관리비", self)
        label6.move(20, 260)

        label7 = QLabel("보증금조정", self)
        label7.move(20, 300)

        label8 = QLabel("입주시기", self)
        label8.move(20, 340)

        # LineEdit
        lineEdit = QLineEdit("", self)
        lineEdit.move(80, 20)
        lineEdit.textChanged.connect(self.lineEditChanged)

        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(80, 60)
        self.lineEdit.textChanged.connect(self.lineEditChanged)

        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(80, 100)
        self.lineEdit.textChanged.connect(self.lineEditChanged)

        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(80, 140)
        self.lineEdit.textChanged.connect(self.lineEditChanged)

        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(80, 180)
        self.lineEdit.textChanged.connect(self.lineEditChanged)

        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(80, 220)
        self.lineEdit.textChanged.connect(self.lineEditChanged)

        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(80, 260)
        self.lineEdit.textChanged.connect(self.lineEditChanged)

        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(80, 300)
        self.lineEdit.textChanged.connect(self.lineEditChanged)

        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(80, 340)
        self.lineEdit.textChanged.connect(self.lineEditChanged)
#푸쉬버튼
        button = QPushButton('작성하기', self)
        button.move(80, 380)
        # button.clicked
        # self.pushbutton(button)
        # button.clicked.connect(QCoreApplication.instance().quit)
        button.clicked.connect(self.pushbutton)
        # button.clicked.connect()
        # StatusBar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

        openFile = QAction('Open', self)
        openFile.triggered.connect(self.pushbutton)

    def pushbutton(self):
        # print("작성하기")
        self.lineEdit.clear()

    def lineEditChanged(self):
        self.statusBar.showMessage(self.lineEdit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()