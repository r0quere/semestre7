import sys
from PyQt5 import QtCore,QtCore,QtGui,QtWidgets,QtSvg

# https://stackoverflow.com/questions/35819538/using-lambda-expression-to-connect-slots-in-pyqt
class Keypad(QtWidgets.QWidget):
    def __init__(self,nbuttons=10,parent=None) :
        super(Keypad, self).__init__()
        self.layout = QtWidgets.QGridLayout(self)
        self.buttons=[]
        self.create_buttons(nbuttons)
        
    # def create_buttons(self,number) :
    #      for i in range(number) :
    #         button=QtWidgets.QPushButton(str(i),self)
    #         button.setCheckable(True)
    #         button.clicked.connect(lambda state,x=i: self.on_selected(state,x))
    #         self.buttons.append(button)
    #         self.layout.addWidget(button)
    def create_buttons(self,number) :
        for i in range(1,number) :
            button=QtWidgets.QPushButton(str(i),self)
            button.setCheckable(True)
            self.layout.addWidget(button,i/3,i%3)
            button.clicked.connect(lambda state,x=i : self.on_selected(state,x) )
            self.buttons.append(button)
            self.layout.addWidget(button)
        button=QtWidgets.QPushButton(str(0),self)
        # button.setCheckable(True)
        button.clicked.connect(lambda state,x=0: self.on_selected(state,x) )
        self.buttons.append(button)
        self.layout.addWidget(button,4,1)
    def on_selected(self,state,index):
        print('state', state)
        print('index', index)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    keypad = Keypad(10)
    keypad.show()
    sys.exit(app.exec_())
