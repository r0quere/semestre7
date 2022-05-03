import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from scene import Scene

class MainWindow (QtWidgets.QMainWindow) :
    def __init__(self,x=0,y=0,width=500,height=400,parent=None):
        QtWidgets.QMainWindow.__init__(self)
#        self.parent=parent
        self.view = QtWidgets.QGraphicsView()
        self.scene = Scene(x,y,width,height,self)
        self.create_scene()
        self.view.setScene(self.scene);
        self.setCentralWidget(self.view)
    def create_scene(self) :
        top_line = QtCore.QLineF(self.scene.sceneRect().topLeft(),self.scene.sceneRect().topRight())
        left_line = QtCore.QLineF(self.scene.sceneRect().topLeft(),self.scene.sceneRect().bottomLeft())
        right_line=QtCore.QLineF(self.scene.sceneRect().topRight(), self.scene.sceneRect().bottomRight())
        bottom_line=QtCore.QLineF(self.scene.sceneRect().bottomLeft(), self.scene.sceneRect().bottomRight())
        pen = QtGui.QPen(QtCore.Qt.red)
        self.scene.addLine(top_line, pen)
        self.scene.addLine(left_line, pen)
        self.scene.addLine(right_line, pen)
        self.scene.addLine(bottom_line, pen)
        text = self.scene.addText("Un texte dans l'application !");
        text.setPos(100,100);
        item = QtWidgets.QGraphicsEllipseItem(0,0,50,50)
        self.scene.addItem(item)
        item = QtWidgets.QGraphicsRectItem(340,240,50,50)
        self.scene.addItem(item)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw=MainWindow()
    mw.show()
##    view = QtWidgets.QGraphicsView()
##    view.setGeometry(QtCore.QRect(0, 0, 600, 500))
####    scene=QtWidgets.QGraphicsScene()
##    scene=Scene()
##    scene.setSceneRect(-150, -150, 300, 300)
##    view.show()
    sys.exit(app.exec_())
