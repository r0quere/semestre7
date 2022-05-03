import sys
from PyQt5 import QtCore,QtGui,QtWidgets

class Scene(QtWidgets.QGraphicsScene) :
    def __init__(self,x=0,y=0,width=500,height=400,parent=None) :
        QtWidgets.QGraphicsScene.__init__(self)
        self.start= self.end = self.offset = QtCore.QPointF(0,0);
#        self.addRect(QtCore.QRectF(50,50,200,300));
        self.item=None
    def mousePressEvent(self,event : QtGui.QMouseEvent) :
        self.start=self.end=event.scenePos();
        self.item=self.itemAt(self.start,QtGui.QTransform())
        if self.item :
            items=self.collidingItems(self.item)
            if event.button()==QtCore.Qt.LeftButton :
                print("left")
                print(items)
                i=0
                while  i< len(items) :
                    items[i].hide()
                    i=i+1
##            elif event.button()==QtCore.Qt.RightButton :         
##                print("right")
##                print(items)
##                i=0
##                while  i< len(items) :
##                    items[i].show();
##                    i=i+1
            self.offset = self.start - self.item.pos()
            self.item.setPos( self.start - self.offset )
            self.item.grabMouse()
        else :
            for item in self.items() :
                item.show()

    def mouseMoveEvent(self,event) :
        if  self.item :
             self.item.setPos(event.scenePos() - self.offset)
        self.end = event.scenePos()
    def mouseReleaseEvent(self,event) :
        if  self.item :
            self.item.setPos(event.scenePos() - self.offset)
            self.item=None
        self.end  = event.scenePos()
        if  self.start!=self.end :
            rect =self.addRect(self.start.x(),
                 self.start.y(),
                 self.end.x() - self.start.x(),
                 self.end.y() - self.start.y())
