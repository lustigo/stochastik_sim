from tkinter import *
from random import randint,shuffle
from Marriage import Marriage
from Atom import Atom
from BubbleGum import BubbleGum
from House_of_Cards import House_of_Cards
from Lotto import Lotto
from SecretSanta import SecretSanta

class Frontend():
    def __init__(self,x,y):
        self.x=str(x)   #1600
        self.y=str(y)   #900
        self.pressed=0
        self.b=10
        self.c=30
    def startwindow(self):
        self.root=Tk()
        a=str(self.x+'x'+self.y)
        self.root.geometry(a)
        self.g=Label(self.root,bg='white')
        self.g.place(x=0,y=0,width=self.x,height=self.y)
        self.lst1 = ['Marriage','Atom','BubbleGum','House_of_Cards','Lotto','SecretSanta']
        self.var1 = StringVar(self.root)
        self.var1.set('Marriage')
        self.drop = OptionMenu(self.root,self.var1,*self.lst1)
        self.drop.config(font=('Arial',(30)),bg='white')
        self.drop['menu'].config(font=('calibri',(20)),bg='white')
        self.drop.pack(side=TOP)
        self.photo = PhotoImage(file='z1.gif')
        self.label = Label(image=self.photo,borderwidth=0)
        self.label.image = self.photo
        self.label.bind('<1>',self.MouseOneDown)
        self.label.place(y=0,x=int(self.x)-200)
        self.startbutton=Button(self.root,text='Start',font=('Arial',40),bg='blue',borderwidth=5,command=self.startpressed)       
        self.startbutton.place(x=0,y=int(self.y)-100,width=int(self.y)-200,height=100)
        self.csvbutton=Button(self.root,text='Export CSV',font=('Arial',40),bg='green',borderwidth=5,command=self.csvpressed)     
        self.csvbutton.place(x=int(self.x)/2+50,y=int(self.y)-100,width=int(self.y)-230,height=100)
    def startpressed(self):
            a=self.var1.get()
            if self.pressed==1:
                self.b=int(self.changer0.get('1.0','end-1c'))
                try:
                    self.c=self.changer2.get('1.0','end-1c')
                except AttributeError:
                    z=0
            if a=='Marriage':
                self.run0=Marriage()
                self.run0.DEBUG=False
                self.run0.sim(self.b)
            elif a=='Atom':
                self.c=float(self.c)
                self.run1=Atom(self.c,self.b)
                self.run1.DEBUG=False
                self.run1.sim()
            elif a=='BubbleGum':
                self.run2=BubbleGum()
                self.run2.sim()
            elif a=='House_of_Cards':
                self.c=int(self.c)
                self.run3=House_of_Cards(self.b,self.c)
                self.run3.sim()
            elif a=='Lotto':
                self.run4=Lotto(self.b)
                self.run4.DEBUG=False
                self.run4.sim()
            elif a=='SecretSanta':
                self.c=int(self.c)
                self.run5=SecretSanta(self.b,self.c)
                self.run5.sim()
    def csvpressed(self):
        a=self.var1.get()
        if a=='Marriage':
            self.run0.exportcsv('Marriage_Template.ods')
        elif a=='Atom':
            self.run1.exportCSV('Atom_Template.ods')
       # elif a=='House_of_Cards':
      #      self.run3.exportCSV('House_of_cards_Template.ods')
        elif a=='Lotto':
            self.run4.exportCSV('Lotto_Template.ods')
    def MouseOneDown(self,event):
        if self.pressed==0:
            a=self.var1.get()
            if a=='Marriage':
                self.changer0=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer0.place(y=100,x=int(self.x)-150,width=100,height=50)
                self.changer1=Label(self.root,text='Versuche:',bg='white',font=('Arial',30),borderwidth=1)
                self.changer1.place(y=100,x=int(self.x)-400,width=250,height=50)
            elif a=='Atom':
                self.changer0=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer0.place(y=100,x=int(self.x)-150,width=100,height=50)
                self.changer1=Label(self.root,text='Anzahl der Atome:',bg='white',font=('Arial',30),borderwidth=1)
                self.changer1.place(y=100,x=int(self.x)-600,width=450,height=50)
                self.changer2=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer2.place(y=200,x=int(self.x)-150,width=100,height=50)
                self.changer3=Label(self.root,text='Zerfallswahrscheinlichkeit:',bg='white',font=('Arial',30),borderwidth=1)
                self.changer3.place(y=200,x=int(self.x)-620,width=450,height=50)
            elif a=='House_of_Cards':
                self.changer0=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer0.place(y=100,x=int(self.x)-150,width=100,height=50)
                self.changer1=Label(self.root,text='Versuche:',bg='white',font=('Arial',30),borderwidth=1)
                self.changer1.place(y=100,x=int(self.x)-400,width=250,height=50)
                self.changer2=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer2.place(y=200,x=int(self.x)-150,width=100,height=50)
                self.changer3=Label(self.root,text='Kartenanzahl(32,55):',bg='white',font=('Arial',30),borderwidth=1)
                self.changer3.place(y=200,x=int(self.x)-620,width=450,height=50)
            elif a=='Lotto':
                self.changer0=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer0.place(y=100,x=int(self.x)-150,width=100,height=50)
                self.changer1=Label(self.root,text='Versuche:',bg='white',font=('Arial',30),borderwidth=1)
                self.changer1.place(y=100,x=int(self.x)-400,width=250,height=50)
            elif a=='SecretSanta':
                self.changer0=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer0.place(y=100,x=int(self.x)-150,width=100,height=50)
                self.changer1=Label(self.root,text='Versuche:',bg='white',font=('Arial',30),borderwidth=1)
                self.changer1.place(y=100,x=int(self.x)-400,width=250,height=50)
                self.changer2=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer2.place(y=200,x=int(self.x)-150,width=100,height=50)
                self.changer3=Label(self.root,text='Anzahl der Schüler:',bg='white',font=('Arial',30),borderwidth=1)
                self.changer3.place(y=200,x=int(self.x)-550,width=400,height=50)
            self.pressed=1
        else:
            self.b=self.changer0.get('1.0','end-1c')
            try:
                self.c=self.changer2.get('1.0','end-1c')
            except (AttributeError,TclError):
                    z=0
            try:
                self.changer3.destroy()
            except AttributeError:
                    z=0
            try:
                self.changer2.destroy()
            except AttributeError:
                    z=0
            self.changer1.destroy()
            self.changer0.destroy()
            self.pressed=0

#a=Frontend(1600,900)
#a.startwindow()
