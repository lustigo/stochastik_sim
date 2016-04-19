from tkinter import *
#from bla import *
#from
def startpressed():
    a=var1.get()
    print(a)
    #if ....
    #elif ....
def csvpressed():
    DieAntwort=42
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
drop['menu'].config(font=('calibri',(200)),bg='white')
drop.pack(side=TOP)
photo = PhotoImage(file='z1.gif')
label = Label(image=photo,borderwidth=0)
label.image = photo 
label.place(y=0,x=int(x)-200)
startbutton=Button(root,text='Start',font=('Arial',40),bg='blue',borderwidth=5,command=startpressed)       #command=start -> var1.get()
startbutton.place(x=0,y=int(y)-100,width=int(y)-200,height=100)
csvbutton=Button(root,text='Export CSV',font=('Arial',40),bg='green',borderwidth=5,command=csvpressed)     #command=exportCSV 
csvbutton.place(x=int(x)/2+50,y=int(y)-100,width=int(y)-200,height=100)
