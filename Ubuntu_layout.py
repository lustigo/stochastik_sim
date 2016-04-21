from tkinter import *
from Marriage import Simulator
#from bla import *
#from
class Frontend():
    def __init__(self,x,y):
        self.x=str(x)   #1080
        self.y=str(y)   #720
        self.pressed=0
        self.b=0
    def startwindow(self):
        self.root=Tk()
        a=str(self.x+'x'+self.y)
        self.root.geometry(a)
        self.g=Label(self.root,bg='white')
        self.g.place(x=0,y=0,width=self.x,height=self.y)
        self.lst1 = ['Option1','Option2fsdfdfs\ns','Option3']
        self.var1 = StringVar(self.root)
        self.var1.set('options')
        self.drop = OptionMenu(self.root,self.var1,*self.lst1)
        self.drop.config(font=('Arial',(30)),bg='white')
        self.drop['menu'].config(font=('calibri',(20)),bg='white')
        self.drop.pack(side=TOP)
        self.photo = PhotoImage(file='z1.gif')
        self.label = Label(image=self.photo,borderwidth=0)
        self.label.image = self.photo
        self.label.bind('<1>',self.MouseOneDown)
        self.label.place(y=0,x=int(self.x)-200)
        self.startbutton=Button(self.root,text='Start',font=('Arial',40),bg='blue',borderwidth=5,command=self.startpressed)       #command=start -> var1.get()
        self.startbutton.place(x=0,y=int(self.y)-100,width=int(self.y)-200,height=100)
        self.csvbutton=Button(self.root,text='Export CSV',font=('Arial',40),bg='green',borderwidth=5,command=self.csvpressed)     #command=exportCSV 
        self.csvbutton.place(x=int(self.x)/2+50,y=int(self.y)-100,width=int(self.y)-230,height=100)
    def startpressed(self):
        a=self.var1.get()
       # try:
      #      self.b=self.changer0.get('1.0','end-1c')
       # except AttributeError:
       #     print('SSSS')
        print(a,self.b)
        #if ....
        #elif ....
    def csvpressed(self):
        sim=Simulator()
        list=[2,3] ######
        sim.exportCSV(list,"test.csv")
    def MouseOneDown(self,event):
        if self.pressed==0:
            self.changer0=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
            self.changer0.place(y=100,x=int(self.x)-150,width=100,height=50)
            self.changer1=Label(self.root,text='Wahrscheinlichkeit:',bg='white',font=('Arial',30),borderwidth=1)
            self.changer1.place(y=100,x=int(self.x)-500,width=350,height=50)
            self.pressed=1
        else:
            self.b=self.changer0.get('1.0','end-1c')
            #
            #
            self.changer1.destroy()
            self.changer0.destroy()
            self.pressed=0

a=Frontend(1080,720)
a.startwindow()
