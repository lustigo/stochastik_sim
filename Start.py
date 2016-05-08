from Ubuntu_layout import Frontend
from tkinter import Tk
#Combines Front&Backend
#does all the magic
b=Tk()
a=Frontend(1080,720,b)
a.startwindow()
b.mainloop()
