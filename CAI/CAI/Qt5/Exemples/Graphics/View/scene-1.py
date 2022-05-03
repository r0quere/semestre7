import sys
from PyQt5 import QtCore,QtGui,QtWidgets

class Scene(QtWidgets.QGraphicsScene) :
    def __init__(self,x=0,y=0,width=600,height=800,parent=None) :
        QtWidgets.QGraphicsScene. __init__(self)
        self.start= self.end = self.offset = QtCore.QPointF(0,0);
        self.addRect(QtCore.QRectF(100,100,200,300));
        self.item=None
    def mousePressEvent(self,event : QtGui.QMouseEvent) :
        self.start=self.end=event.scenePos();
        self.item=self.itemAt(self.start,QtGui.QTransform())
##        if event.key() == Qt.Key_Escape:
##
        if event.button()==QtCore.Qt.LeftButton :         
            if self.item :
                items=self.collidingItems(self.item)
                print(items)
                i=0
                while  i< len(items) :
                    items[i].hide();
                    i=i+1
                self.offset = self.start - self.item.pos();
                self.item.setPos( self.start - self.offset );
                self.item.grabMouse();
            else :
                for item in self.items() :
                    item.show()
        else :
            print("right")
             
    def mouseMoveEvent(self,event) :
        if  self.item :
             self.item.setPos(event.scenePos() - self.offset);
        self.end = event.scenePos();
    def mouseReleaseEvent(self,event) :
        if  self.item :
            self.item.setPos(event.scenePos() - self.offset);
            self.item.grabMouse();
            self.item=None
        elif  self.start !=self.end :
            rect =self.addRect(self.start.x(),
                 self.start.y(),
                 self.end .x() - self.start.x(),
                 self.end .y() - self.start.y());
            rect.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable);
        self.end  = event.scenePos();
