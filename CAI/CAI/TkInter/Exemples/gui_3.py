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

# Définition des actions, comportements (callbacks)
def app_exit(event) :
    mw.destroy()
def mouse_location(event,label):
    label.configure(text= "Position X ="+str(event.x)+ ", Y ="+ str(event.y))

# Création de l'IHM
def gui(parent) :
    # arbre des composants graphiques
    canvas=tk.Canvas(parent,width=200,height=150,bg="light yellow")
    data=tk.Label(parent,text="Mouse Location")
    hello=tk.Label(parent,text="Hello World !",fg="blue")
    button_quit=tk.Button(parent,text="Goodbye World", fg="red")
    # positionnement des composants (layout manager)
    hello.pack()
    canvas.pack()
    data.pack()
    button_quit.pack()
    # interaction : liaison Composant-Evenement-Action 
    button_quit.bind("<Button-1>",app_exit)
    canvas.bind("<Motion>",lambda event,label=data : mouse_location(event,label))

if __name__ =="__main__" :
    mw=tk.Tk()
    gui(mw)
    mw.mainloop()