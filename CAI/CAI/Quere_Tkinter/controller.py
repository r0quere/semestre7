# -*- coding: utf-8 -*-
from cProfile import label
from cgitb import text
from cmath import phase
from msilib.schema import File
from pickle import FRAME
from re import X
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
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
import json
# import logging
# logging.basicConfig(level=logging.DEBUG)
# # logging.basicConfig(level=logging.CRITICAL)
# logger = logging.getLogger(__name__)

class Controller (object):
    mag = 0,5
    harmonics=1
    signal = []
    name = ""
    # canvas = None
    def __init__(self,model,view, parent,mag = 0.5):
        self.parent=parent
        self.model,self.view = model,view
        self.create_controls()
        # self.packing()
        self.mag=mag
        self.packing()
        self.signal = model.signal
        self.name = model.name
        self.parent.option_readfile("config.opt")

        if self.parent :
            self.parent=parent
            menu = tk.Menu(parent)
            parent.config(menu=menu)
            fileMenu = tk.Menu(menu)
            fileMenu.add_command(label="Save",command=self.save)
            fileMenu.add_command(label="open",command=self.open)
            fileMenu.add_command(label="Exit_sans_avertissement", command=self.close_app)
            fileMenu.add_command(label="Exit_avec_avertissement", command=self.close_app_demande)
            menu.add_cascade(label="File", menu=fileMenu)
 
            fileMenu = tk.Menu(menu)
            fileMenu.add_command(label="About Us ...",command=self.about_us)
            fileMenu.add_command(label="About Python  ...",command=self.about_python)
            fileMenu.add_command(label="About TK  ...",command=self.about_TK)
            fileMenu.add_command(label="Readme  ...",command=self.readme)
            menu.add_cascade(label="Help", menu=fileMenu)
        self.packing()
        
    def save(self):
    #       f = asksaveasfile(initialfile = 'param-signal.txt',
    #   defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])7
        path = './'

        phaseSave = self.model.get_phase()
        ampliSave = self.model.get_magnitude()
        freqSave = self.model.get_frequency()
        harmSave = self.model.get_harmonics()
        data = {}
        data['phase'] = phaseSave
        data['amplitude'] = ampliSave
        data['frequency'] = freqSave
        data['harmonics'] = harmSave
        files = [('JSON File', '*.json')]
        fileName = "Sauvegarde_param"
        filepos = asksaveasfile(filetypes = [("All Files","."),("Text Documents",".txt")],title="Save...",defaultextension = json,initialfile='Sauvegarde_param')
        print(filepos)
        json.dump(data, filepos)


    def open(fp):
        filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       


    def close_app(self):
        exit()

    def close_app_demande(self):
        res = messagebox.askyesno('prompt', 'fermer?') 
        if res == True:
            exit()

        elif res == False:
            pass
        else:
            messagebox.showerror('error', 'erreur!')

    def about_us(self):
        print("about_us %s" % "QUERE")
        messagebox.showinfo('About Us', "Quere Romain r0quere@enib.fr")
    
    def about_TK(self):
        print("about_TK %s" % "TkInter")
        messagebox.showinfo('About TK', "Tkinter est la bibliothèque graphique libre d'origine pour le langage Python, permettant la création d'interfaces graphiques. Elle vient d'une adaptation de la bibliothèque graphique Tk écrite pour Tcl")

    def readme(self):
        print("readme %s" % "readme")
        messagebox.showinfo('jai eu quelque difficulté quant à la mise en place de la sauvegarde et de open')

    def about_python(self):
        print("about_python %s" % "version de python 3.9.7")
        messagebox.showinfo('About Python', "version de python 3.9.7")

    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
    def get_magnitude(self):
        return self.mag
    def set_magnitude(self,mag):
        self.mag=mag
    def get_frequency(self):
        return self.freq
    def set_frequency(self,freq):
        self.freq=freq
    def get_phase(self):
        return self.phase
    def set_phase(self,phase):
        self.phase=phase
    def get_harmonics(self) :
        return self.harmonics    
    def set_harmonics(self,harmonics=1) :
        self.harmonics=harmonics
    def get_samples(self):
        return self.samples
    def set_samples(self,samples):
        self.samples=samples
         
    def delete(self):
        del self.signal[0:]
        self.notify()

    def packing(self) :
       # self.canvas.pack(expand=1,fill="both",padx=6)
        self.scale_magX.pack()
        self.scale_harmonicsX.pack()
        self.scale_phaseX.pack()
        self.scale_freqX.pack()

        self.scale_magY.pack()
        self.scale_harmonicsY.pack()
        self.scale_phaseY.pack()
        self.scale_freqY.pack()

        # self.frameX.pack(side="left",expand=True,fill="x")
        self.frameX.pack(side="left",expand=True,fill="y")
        self.frameY.pack(side="right",expand=True,fill="y")



    def create_controls(self):
        self.frameX=tk.LabelFrame(self.parent,text="X",name="frameX")
        self.frameY=tk.LabelFrame(self.parent,text="Y",name="frameY")

        self.mag=tk.IntVar()
        self.mag.set(1)

        self.phase_varX=tk.DoubleVar()
        self.phase_varX.set(self.get_magnitude())
        self.scale_phaseX=tk.Scale(self.frameX,variable=self.phase_varX,
                          label="Phase",
                          orient="horizontal",length=250,
                          from_=-90,to=90,relief="raised",
                          sliderlength=20,resolution = 0.1,
                          tickinterval=20,
                          command=self.cb_update_phase_X)   

        self.freq_varX=tk.DoubleVar()
        self.freq_varX.set(self.get_magnitude())
        self.scale_freqX=tk.Scale(self.frameX,variable=self.freq_varX,
                          label="Frequence",
                          orient="horizontal",length=250,
                          from_=0,to=50,relief="raised",
                          sliderlength=20,resolution = 0.1,
                          tickinterval=10,
                          command=self.cb_update_frequency_X)
        self.mag_varX=tk.DoubleVar()
        self.mag_varX.set(self.get_magnitude())
        self.scale_magX=tk.Scale(self.frameX,variable=self.mag_varX,
                          label="Amplitude",
                          orient="horizontal",length=250,
                          from_=0,to=1,relief="raised",
                          sliderlength=20,resolution = 0.1,
                          tickinterval=0.5,
                          command=self.cb_update_magnitude_X)
        self.harmonics_varX=tk.IntVar()
        self.harmonics_varX.set(self.get_harmonics())
        self.scale_harmonicsX=tk.Scale(self.frameX,variable=self.harmonics_varX,
                          label="Harmonics",
                          orient="horizontal",length=250,
                          from_=1,to=50,relief="raised",
                          sliderlength=20,tickinterval=5,
                          command=self.cb_update_harmonics_X)
        frame=tk.LabelFrame(self.frameX,text="Harmonics")
        self.radio_var=tk.IntVar()
        
        btn=tk.Radiobutton(frame,text="All", variable=self.radio_var,value=1,command=self.cb_activate_button)
        btn.select()
        btn.pack(anchor ="w")
        btn=tk.Radiobutton(frame,text="Odd", variable=self.radio_var,value=2,command=self.cb_activate_button)
        btn.pack(anchor ="w")
        frame.pack()
        


        self.phase_varY=tk.DoubleVar()
        self.phase_varY.set(self.get_magnitude())
        self.scale_phaseY=tk.Scale(self.frameY,variable=self.phase_varY,
                          label="Phase",
                          orient="horizontal",length=250,
                          from_=-90,to=90,relief="raised",
                          sliderlength=20,resolution = 0.1,
                          tickinterval=20,
                          command=self.cb_update_phase_Y)   
        self.freq_varY=tk.DoubleVar()
        self.freq_varY.set(self.get_magnitude())
        self.scale_freqY=tk.Scale(self.frameY,variable=self.freq_varY,
                          label="Frequence",
                          orient="horizontal",length=250,
                          from_=0,to=50,relief="raised",
                          sliderlength=20,resolution = 0.1,
                          tickinterval=10,
                          command=self.cb_update_frequency_Y)
        self.mag_varY=tk.DoubleVar()
        self.mag_varY.set(self.get_magnitude())
        self.scale_magY=tk.Scale(self.frameY,variable=self.mag_varY,
                          label="Amplitude",
                          orient="horizontal",length=250,
                          from_=0,to=1,relief="raised",
                          sliderlength=20,resolution = 0.1,
                          tickinterval=0.5,
                          command=self.cb_update_magnitude_Y)

        self.harmonics_varY=tk.IntVar()
        self.harmonics_varY.set(self.get_harmonics())
        self.scale_harmonicsY=tk.Scale(self.frameY,variable=self.harmonics_varY,
                          label="Harmonics",
                          orient="horizontal",length=250,
                          from_=1,to=50,relief="raised",
                          sliderlength=20,tickinterval=5,
                          command=self.cb_update_harmonics_Y)
        frame=tk.LabelFrame(self.frameY,text="Harmonics")
        self.radio_var=tk.IntVar()

        btn=tk.Radiobutton(frame,text="All", variable=self.radio_var,value=1,command=self.cb_activate_button)
        btn.select()
        btn.pack(anchor ="w")
        btn=tk.Radiobutton(frame,text="Odd", variable=self.radio_var,value=2,command=self.cb_activate_button)
        btn.pack(anchor ="w")
        frame.pack()
        

    def cb_update_magnitude_X(self,event):
        print("cb_update_magnitude(self,event)",self.mag_varX.get())
        self.model.set_magnitude(self.mag_varX.get())
        self.model.generate()
        # sself.view.plot_signal(self.signal,self.name)

    def cb_update_magnitude_Y(self,event):
        print("cb_update_magnitude(self,event)",self.mag_varY.get())
        self.model.set_magnitude(self.mag_varY.get())
        self.model.generate()

    def cb_update_phase_X(self,event):
        print("cb_update_phase(self,event)",self.phase_varX.get())
        self.model.set_phase(self.phase_varX.get())
        self.model.generate()

    def cb_update_phase_Y(self,event):
        print("cb_update_phase(self,event)",self.phase_varY.get())
        self.model.set_phase(self.phase_varY.get())
        self.model.generate()


    def cb_update_frequency_X(self,event):
        print("cb_update_frequency(self,event)",self.freq_varX.get())
        self.model.set_frequency(self.freq_varX.get())
        self.model.generate()

    def cb_update_frequency_Y(self,event):
        print("cb_update_frequency(self,event)",self.freq_varY.get())
        self.model.set_frequency(self.freq_varY.get())
        self.model.generate()

    def cb_update_harmonics_X(self,event):
        print("cb_update_harmonics(self,event)",self.harmonics_varX.get())
        self.model.set_harmonics(self.harmonics_varX.get())
        self.model.generate()
        # self.view.plot_signal(self.signal,self.name)

    def cb_update_harmonics_Y(self,event):
        print("cb_update_harmonics(self,event)",self.harmonics_varY.get())
        self.model.set_harmonics(self.harmonics_varY.get())
        self.model.generate()
        # self.view.plot_signal(self.signal,self.name)

    def cb_activate_button(self):
        print("You selected the option " + str(self.radio_var.get()))
        self.model.harmo_odd_even=self.radio_var.get()