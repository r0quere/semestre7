import sys
print("Your platform is : " ,sys.platform)
major=sys.version_info.major
minor=sys.version_info.minor
print("Your python version is : ",major,minor)
if major==2 and minor==7 :
    import Tkinter as tk
    import tkFileDialog as filedialog
elif major==3 and minor==6 :
    import tkinter as tk
    from tkinter import filedialog
else :
    print("with your python version : ",major,minor)
    print("... I guess it will work !")
    import tkinter as tk
    from tkinter import filedialog
    
import tkinter.ttk as ttk
 
def print_something(event):
	print("You choose " + v.get())
 
root = tk.Tk()
v = tk.StringVar()
om = ttk.OptionMenu(root, v, "Choose", "item 1", "item 2", "item 3")
v.set("item 3")
om.pack()
om.bind("<Return>", print_something)
om.focus()
 
root.mainloop()
