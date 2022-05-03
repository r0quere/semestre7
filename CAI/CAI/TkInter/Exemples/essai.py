import sys
major=sys.version_info.major
minor=sys.version_info.minor
if major==2 and minor==7 :
    import Tkinter as tk
    import tkFileDialog as filedialog
elif major==3 and minor==6 :
    import tkinter as tk
    from tkinter import filedialog
else :
    print("Your python version is : ",major,minor)
    print("... I guess it will work !")
    import tkinter as tk
    from tkinter import filedialog 

if __name__ =="__main__" :
    mw=tk.Tk()
    label_hello=tk.Label(mw,text="Hello World !",fg="blue")
    button_quit=tk.Button(mw, text="Goodbye World", fg="red",command=mw.destroy)
    label_hello.pack()
    button_quit.pack()
    mw.mainloop()
