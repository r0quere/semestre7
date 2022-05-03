#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import json
import pickle

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QT_VERSION_STR

def data_to_items(scene,data):
    scene.clear()
    print("data",data)
    for d_item in data :
        print("d_item",d_item)
        t = d_item["type"]
        if t == "line":
            x1, y1, x2, y2 = d_item["x1"], d_item["y1"], d_item["x2"], d_item["y2"]
            scene.addLine(x1, y1, x2, y2)

def load_scene(scene,name) :
    # file_to_load=open(name,"rb")
    # data=pickle.load(file_to_load)
    # data_to_items(scene,data)
    # file_to_load.close()
    file_to_save = QtCore.QFile(filename)
    if file_to_save.open(QtCore.QIODevice.WriteOnly):
        file_to_save.write(json.dumps(data).encode("utf-8"))
        file_to_save.close()
        
if __name__ == "__main__":
    print(QT_VERSION_STR)
    app   = QtWidgets.QApplication(sys.argv)
    scene=QtWidgets.QGraphicsScene()
    filename="scene.pkl"
    #------------- scene creation --------------------
    load_scene(scene,filename) 
    #-------------------------------------------------
    view=QtWidgets.QGraphicsView(scene)
    filename="scene.json"
    open(filename)
    view.show()
    sys.exit(app.exec_())
