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

from math import pi,sin

class Screen :
    def __init__(self,parent,bg="white",width=600,height=300):
        self.canvas=tk.Canvas(parent, bg=bg,width=width,height=height)
        self.a,self.f,self.p=1.0,2.0,0.0
        self.signal=[]
        self.width,self.height=width,height
        self.units=1
        self.canvas.bind("<Configure>",self.resize)
    def vibration(self,t,harmoniques=1):
        a,f,p=self.a,self.f,self.p
        somme=0
        for h in range(1,harmoniques+1) :
            somme=somme + (a/h)*sin(2*pi*(f*h)*t-p)
        return somme
    def generate_signal(self,period=10,samples=1000):
        del self.signal[0:]
        echantillons=range(int(samples)+1)
        Tech = period/samples
        for t in echantillons :
            self.signal.append(
                    [t*Tech,self.vibration(t*Tech)]
                            )
        return self.signal
    def update(self):
        self.generate_signal()
        if self.signal :
            self.plot_signal(self.signal)
    def plot_signal(self,signal,color="red"):
        w,h=self.width,self.height
        signal_id=None
        if signal and len(signal) > 1:
            plot=[(x*w,h/2.0*(1-y/(self.units/2))) for (x,y) in signal]
        signal_id=self.canvas.create_line(plot,fill=color,smooth=1,width=3,tags="curve")
        return signal_id
    def grid(self,tiles=2):
        self.units=tiles
        tile_x=self.width/tiles
        for t in range(1,tiles+1):
            x =t*tile_x
            self.canvas.create_line(x,0,x,self.height,tags="grid")
            self.canvas.create_line(x,self.height/2-10, x,self.height/2+10,width=3,tags="grid")
        tile_y=self.height/tiles
        for t in range(1,tiles+1):
            y =t*tile_y
            self.canvas.create_line(0,y,self.width,y,tags="grid")
            self.canvas.create_line(self.width/2-10,y,self.width/2+10,y, width=3,tags="grid")
    def resize(self,event):
        if event:
            self.width,self.height=event.width,event.height
            self.canvas.delete("grid")
            self.canvas.delete("curve")
            self.plot_signal(self.signal)
            self.grid(self.units)
    def packing(self) :
        self.canvas.pack(expand=1,fill="both",padx=6)

if   __name__ == "__main__" :
   mw=tk.Tk()
   view=Screen(mw)
   view.grid(8)
   view.packing()
   view.update()
   mw.mainloop()

