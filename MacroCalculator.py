import sys
from PyQt5.QtWidgets import *
#from PyQt5 import QtGui

app = QApplication(sys.argv)
widget = QWidget()
label = QLabel("", widget)

btnAdd = QPushButton("Add", widget)
btnSub = QPushButton("Subtract", widget)
btnDiv = QPushButton("Divide", widget)
btnMul = QPushButton("Multiply", widget)


#txtArea = QPlainTextEdit("Text To Edit", widget)widget.resize

txtBodyWeight = QLineEdit("Body Weight (in LBS)", widget)
txtActivityLevel = QLineEdit("Activity Level", widget)

def init():

    widget.resize(300, 300)
    widget.move(300, 300)
    widget.setWindowTitle('Macro Calculator')
    widget.show()

    txtBodyWeight.move(90,10)
    txtBodyWeight.show()
    txtActivityLevel.move(90,60)
    txtActivityLevel.show()

    label.setText("")
    label.move(20,110)
    label.show()

    btnAdd.setToolTip('Addition')
    btnAdd.move(20,160)
    btnAdd.clicked.connect(addition)
    btnAdd.show()

    btnSub.setToolTip('Subtraction')
    btnSub.move(110,160)
    btnSub.clicked.connect(subtraction)
    btnSub.show()

    btnDiv.setToolTip('Division')
    btnDiv.move(20,210)
    btnDiv.clicked.connect(division)
    btnDiv.show()

    btnMul.setToolTip('Multiplication')
    btnMul.move(110,210)
    btnMul.clicked.connect(multiplication)
    btnMul.show()


def addition():
    num1 = int(txtBodyWeight.text())
    num2 = int(txtActivityLevel.text())
    label.setFixedWidth(200)
    label.setText("Addition: "+str(num1 + num2))

def subtraction():
    num1 = int(txtBodyWeight.text())
    num2 = int(txtActivityLevel.text())
    label.setFixedWidth(200)
    label.setText("Subtraction: "+str(num1 - num2))

def multiplication():
    num1 = int(txtBodyWeight.text())
    num2 = int(txtActivityLevel.text())
    label.setFixedWidth(200)
    label.setText("Multiplication: "+str(num1 * num2))

def division():
    num1 = int(txtBodyWeight.text())
    num2 = int(txtActivityLevel.text())
    label.setFixedWidth(200)
    label.setText("Division: "+str(num1 / num2))

if __name__ == "__main__":
     init()

app.exec_()
