# -*- coding: utf-8 -*-
import json
import sys
from tkinter import Tk, Toplevel, messagebox
from tkinter.ttk import Label
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

from observer import Observer


class Screen(Observer) :
    def __init__(self,parent,bg="white",name="signal",mag=0.5,freq=2.0,phase=0.0,harmonics=1):
        self.parent = parent
        self.name=name
        self.mag,self.freq,self.phase,self.harmonics=mag,freq,phase,harmonics
        self.signal=[]
        self.signal1=[]
        self.signals=[]
        self.harmo_odd_even=1
        self.samples=100
        self.canvas=tk.Canvas(parent,bg=bg)
        self.canvas.bind("<Configure>", self.resize)
        self.width=int(self.canvas.cget("width"))
        self.height=int(self.canvas.cget("height"))
        self.resize=False
        self.tiles=4
        self.plot_signal(self.signal)
        self.plot_signal(self.signal1)
        self.create_grid()
        self.packing()


        # tk.Frame.__init__(self, borderwidth=2)

    def plot_signal(self,signal,name="signal",color="red",erase=False):
        width,height=self.width,self.height
        if signal and len(signal)>1:
            self.canvas.delete(name)
            plot=[(x*width, height/2*(y+1)) for (x,y) in signal]
            self.canvas.create_line(plot,fill=color,smooth=1,width=3,tags=name)

    def plot_signals(self):
        for name,signal in self.signals.items():
            self.canvas.delete(name)
            self.plot_signal(name,signal)
        return

     

    def create_grid(self):
        width,height=self.width,self.height
        tiles=self.tiles
        tile_x=width/tiles
        for t in range(1,tiles+1):          # lignes verticales
            x=t*tile_x
            self.canvas.create_line(x,0,x,height,tags="grid")
            self.canvas.create_line(x,height/2-5,x,height/2+5 ,width=4,tags="grid")
        tile_y=height/tiles
        for t in range(1,tiles+1):        # lignes horizontales
            y=t*tile_y
            self.canvas.create_line(0,y,width,y,tags="grid")
            self.canvas.create_line(width/2-5,y,width/2+5,y,width=4,tags="grid")

    def resize(self, event):
        self.width = event.width
        self.height = event.height
        print("resize : ",self.width,self.height)
        self.canvas.delete("grid")
        self.create_grid()
        self.plot_signal(self.signal,self.name)

    def packing(self) :
        self.canvas.pack(expand=1,fill="both",padx=6)
        # self.scale_mag.pack()
        # self.scale_harmonics.pack()
    
    def update(self, model):
        self.signal=model.get_signal()
        self.plot_signal(self.signal)
        self.signal1=model.get_signal1()
        self.plot_signal(self.signal1)
    
if   __name__ == "__main__" :
    root=tk.Tk()
    root.title("QUERE : X-Y Simulator")
    simulator=Screen(root)
    #simulator.set_tiles(tiles=10)
    simulator.create_grid()
    #simulator.plot_signal(simulator.get_signal(),simulator.get_name())
    simulator.packing()
    root.mainloop()