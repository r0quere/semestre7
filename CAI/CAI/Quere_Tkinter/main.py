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
    if __name__ == "__main__" :
        print("Your python version is : ",major,minor)
        print("... I guess it will work !")
    import tkinter as tk
    from tkinter import filedialog 

from math import pi,sin
from utils import radians
# import logging
# logging.basicConfig(level=logging.DEBUG)
# # logging.basicConfig(level=logging.CRITICAL)
# logger = logging.getLogger(__name__)

from generator import Generator
from controller import Controller
from screen import Screen

if   __name__ == "__main__" :
    root=tk.Tk()
    root.title("Quere : X-Y Simulator")
    root.option_readfile("config.opt")
    model = Generator(root)
    view = Screen(root)
    view.update(model)
    model.attach(view)
    ctrl = Controller(model,view,root)
    root.option_readfile("config.opt")



    root.mainloop()