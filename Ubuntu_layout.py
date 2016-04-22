from tkinter import *
from Marriage import Simulator
#from bla import *
#from
pressed=0
def startpressed():
    a=var1.get()
    print(a)
    #if ....
    #elif ....
def csvpressed():
    sim=Simulator()
    list=[2,3] ######
    sim.exportCSV(list,"test.csv")
def MouseOneDown(event):
    global pressed,changer0,changer1
    if pressed==0:
        changer0=Text(root,bg='white',font=('Arial',30),borderwidth=1)
        changer0.place(y=100,x=int(x)-150,width=100,height=50)
        changer1=Label(root,text='Wahrscheinlichkeit:',bg='white',font=('Arial',30),borderwidth=1)
        changer1.place(y=100,x=int(x)-500,width=350,height=50)
        pressed=1
    else:
        #
        #
        #
        changer1.destroy()
        changer0.destroy()
        pressed=0
root=Tk()
x=str(1080)
y=str(720)
a=str(x+'x'+y)
root.geometry(a)
g=Label(root,bg='white')
g.place(x=0,y=0,width=x,height=y)
lst1 = ['Option1','Option2fsdfdfs\ns','Option3']
var1 = StringVar(root)
var1.set('options')
drop = OptionMenu(root,var1,*lst1)
drop.config(font=('Arial',(30)),bg='white')
drop['menu'].config(font=('calibri',(20)),bg='white')
drop.pack(side=TOP)
photo = PhotoImage(file='z1.gif')
label = Label(image=photo,borderwidth=0)
label.image = photo
label.bind('<1>',MouseOneDown)
label.place(y=0,x=int(x)-200)
startbutton=Button(root,text='Start',font=('Arial',40),bg='blue',borderwidth=5,command=startpressed)       #command=start -> var1.get()
startbutton.place(x=0,y=int(y)-100,width=int(y)-200,height=100)
csvbutton=Button(root,text='Export CSV',font=('Arial',40),bg='green',borderwidth=5,command=csvpressed)     #command=exportCSV 
csvbutton.place(x=int(x)/2+50,y=int(y)-100,width=int(y)-230,height=100)
