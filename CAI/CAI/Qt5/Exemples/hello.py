import sys
from PyQt5 import QtWidgets
# from PySide import QtWidgets

def gui(parent):
    button=QtWidgets.QLabel(parent)
    button.setText("Hello World !")
    button.move(100,50)
    button.setStyleSheet("background-color:yellow;")
if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    mw=QtWidgets.QWidget()
    mw.setGeometry(300,150,300,400)
    mw.setWindowTitle("PyQt5 : Hello 1")
    gui(mw)
    mw.show()
    sys.exit(app.exec_())
