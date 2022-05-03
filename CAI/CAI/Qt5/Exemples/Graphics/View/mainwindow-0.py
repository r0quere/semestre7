import sys
from PyQt5 import QtCore,QtGui,QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = QtWidgets.QGraphicsView()
    view.setGeometry(QtCore.QRect(0, 0, 500, 400))
    view.setWindowTitle("CAI : Graphics View");
    scene=QtWidgets.QGraphicsScene()
    scene.setSceneRect(0,0,400,300)
    top_line = QtCore.QLineF(scene.sceneRect().topLeft(),scene.sceneRect().topRight())
    left_line = QtCore.QLineF(scene.sceneRect().topLeft(),scene.sceneRect().bottomLeft())
    right_line=QtCore.QLineF(scene.sceneRect().topRight(), scene.sceneRect().bottomRight())
    bottom_line=QtCore.QLineF(scene.sceneRect().bottomLeft(), scene.sceneRect().bottomRight())

    pen = QtGui.QPen(QtCore.Qt.red)
    
    scene.addLine(top_line,pen)
    scene.addLine(left_line,pen)
    scene.addLine(right_line,pen)
    scene.addLine(bottom_line,pen)

    view.setScene(scene)
    item = QtWidgets.QGraphicsEllipseItem(0,0,50,50)
    scene.addItem(item)
    item = QtWidgets.QGraphicsRectItem(340,240,50,50)
    scene.addItem(item)
    view.show()
    sys.exit(app.exec_())
