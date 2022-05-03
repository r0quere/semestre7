# coding: utf-8
import sys
major=sys.version_info.major
minor=sys.version_info.minor
if major==2 and minor==7 :
    import Tkinter as tk
    import tkFileDialog as filedialog
elif major==3 :
    import tkinter as tk
    from tkinter import filedialog
else :
    print("Your python version is : ",major,minor)
    print("... I guess it will work !")
    import tkinter as tk
    from tkinter import filedialog 

from observer import *
class Model(Subject):
    def __init__(self, names=[]):
        Subject.__init__(self)
        self.__data = names
    def get_data(self):
        return self.__data
    def insert(self,name):
        self.__data.append(name)
        self.notify()            # Observer.update() calls
    def delete(self, index):
        del self.__data[index]
        self.notify()            #  # Observer.update() calls
class View(Observer):
    def __init__(self,parent):
        self.parent=parent
        self.list=tk.Listbox(parent)
        self.list.configure(height=4)
        self.entry=tk.Entry(parent)
        self.layout()
    def update(self,model):        # call by Model.notify()
        self.list.delete(0, "end")
        for data in model.get_data():
            self.list.insert("end", data)
    def layout(self) :
        self.list.pack()
        self.entry.pack()

class Controller(object):
    def __init__(self,model,view):
        self.model,self.view = model,view
        self.view.entry.bind("<Return>",self.enter_action)
        self.view.list.bind("<Delete>",self.delete_action)
    def enter_action(self, event):
        data = self.view.entry.get()
        self.model.insert(data)
    def delete_action(self, event):
        for index in self.view.list.curselection():
            self.model.delete(int(index))

if __name__ =="__main__" :
    mw=tk.Tk()
    mw.title("Men")
    names=["Jean", "John", "Joe"]
    model = Model(names)
    view = View(mw)
    view.update(model)
    model.attach(view)
    ctrl = Controller(model,view)

    top = tk.Toplevel()
    top.title("Men")
    view = View(top)
    view.update(model)
    model.attach(view)
    ctrl = Controller(model,view)

    top = tk.Toplevel()
    top.title("Women")
    # names=["Jeanne", "Joanna", "Jeanette"]
    # model = Model(names)
    view = View(top)
    view.update(model)
    model.attach(view)
    ctrl = Controller(model,view)
 
    mw.mainloop()
    exit(0)
