from tkinter import Tk, Label, StringVar,OptionMenu,TOP,PhotoImage,Button,Text,TclError
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
        self.grapher=0
        self.graph=[0,0,0,0]
    def startwindow(self):
        self.root=Tk()
        a=str(self.x+'x'+self.y)
        self.root.title('Wahrscheinlichkeinten & Simulation')
        self.root.geometry(a)
        self.g=Label(self.root,bg='white')
        self.g.place(x=0,y=0,width=self.x,height=self.y)
       # self.g.bind('<1>',self.optioncanged)
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
        self.startbutton=Button(self.root,text='Start',font=('Arial',40),bg='#B4045F',borderwidth=5,command=self.startpressed)       
        self.startbutton.place(x=0,y=int(self.y)-100,width=int(self.y)-200,height=100)
        self.csvbutton=Button(self.root,text='Export CSV',font=('Arial',40),bg='green',borderwidth=5,command=self.csvpressed)     
        self.csvbutton.place(x=int(self.x)/2+50,y=int(self.y)-100,width=int(self.y)-230,height=100)
    def startpressed(self):
            if self.grapher==1:
                for x in range(len(self.graph)):
                    if self.graph[x]!=0:
                        self.graph[x].destroy()
                self.grapher=0
                self.root.update()
            a=self.var1.get()
            if self.pressed==1:
                try:
                    self.b=int(self.changer0.get('1.0','end-1c'))
                except (AttributeError,TclError,ValueError):
                    self.b=10
                try:
                    self.c=self.changer2.get('1.0','end-1c')
                except (AttributeError,TclError,ValueError):
                    self.c=1
            if a=='Marriage':
                self.run0=Marriage(self.b)
                self.run0.DEBUG=False
                self.run0.sim()
            elif a=='Atom':
                self.c=float(self.c)
                self.run1=Atom(self.c,self.b)
                self.run1.DEBUG=False
                self.run1.sim()
            elif a=='BubbleGum':
                self.run2=BubbleGum(self.b)
                self.run2.DEBUG=False
                self.run2.sim()
                self.grapher=1
                self.graph=[0]
                self.graph[0]=Label(self.root,bg='white',text=('Durchschnitt: '+str(round(self.run2.getrel(),4))),font=('calibri',19))
                self.graph[0].place(x=10,y=450)
            elif a=='House_of_Cards':
                if self.c=='':
                    self.c=0
                else:
                    self.c=int(self.c)
                self.run3=House_of_Cards(self.b,self.c)
                self.run3.DEBUG=False
                self.run3.sim()
                self.grapher=1
                self.graph=[0]
                self.graph[0]=Label(self.root,bg='white',text=('Durchschnitt: '+str(round(self.run3.getrel(),4))),font=('calibri',19))
                self.graph[0].place(x=10,y=450)
            elif a=='Lotto':
                self.run4=Lotto(self.b)
                self.run4.DEBUG=False
                self.run4.sim()
                x=4
                y=1
                count=0
                self.graph=[0,0,0,0]
                self.grapher=1
                self.graph[0]=Label(self.root,bg='black')
                self.graph[0].place(x=10,width=10+(int(self.x)*0.8),height=1,y=int(self.y)-int(self.y)/4*0.5-350)
                self.graph[1]=Label(self.root,text='50%',bg='white',font=('calibri',10))
                self.graph[1].place(x=60+(int(self.x)*0.8),width=50,height=50,y=int(self.y)-int(self.y)/4*0.5-375)
                self.graph[2]=Label(self.root,bg='black')
                self.graph[2].place(x=10,width=20,height=1,y=int(self.y)-350)
                self.graph[3]=Label(self.root,bg='black')
                self.graph[3].place(x=10,width=20,height=1,y=int(self.y)-int(self.y)/4-350)
                for draw in self.run4.turns:
                    if draw.count(0) == 0:
                        count += 1
                    elif draw.count(1) == 0:
                        count += 1
                    elif draw.count(2) == 0:
                        count += 1
                    elif draw.count(3) == 0:
                        count += 1
                    elif draw.count(4) == 0:
                        count += 1
                    elif draw.count(5) == 0:
                        count += 1
                    self.graph+=[0]
                    self.graph[x]=Label(self.root,bg='red')
                    if str(self.c)=='1':
                        self.graph[x].place(x=int(10+(int(self.x)*0.8)*((y-1)/self.b)),width=int(1250/self.b),height=int(self.y)-350-(int(int(self.y)-int(self.y)/4*(count/y)-350)),y=int(int(self.y)-int(self.y)/4*(count/y)-350))
                    else:
                        self.graph[x].place(x=int(10+(int(self.x)*0.8)*(y/self.b)),width=3,height=3,y=int(int(self.y)-int(self.y)/4*(count/y)-350))
                    x+=1
                    y+=1
                    self.root.update()
            elif a=='SecretSanta':
                if self.c=='':
                    self.c=1
                else:
                    self.c=int(self.c)
                self.run5=SecretSanta(self.b,self.c)
                self.run5.DEBUG=False
                self.run5.sim()
                self.grapher=1
                self.graph=[0]
                self.graph[0]=Label(self.root,bg='white',text=('Durchschnitt: '+str(round(self.run5.getrel(),4))),font=('calibri',19))
                self.graph[0].place(x=10,y=450)
    def csvpressed(self):
        a=self.var1.get()
        if a=='Marriage':
            self.run0.exportcsv('Marriage_Simulation.csv')
        elif a=='Atom':
            self.run1.exportCSV('Atom_Simulation.csv')
        elif a=='Lotto':
            self.run4.exportCSV('Lotto_Simulation.csv')
  #  def optioncanged(self,event):
  #          a=self.var1.get()
   #         if a=='Marriage':
    #            self.csvbutton.destroy()
     #           self.csvbutton=Button(self.root,text='Export CSV',font=('Arial',40),bg='green',borderwidth=5,command=self.csvpressed)     
          #      self.csvbutton.place(x=int(self.x)/2+50,y=int(self.y)-100,width=int(self.y)-230,height=100)
      #      elif a=='Atom':
       #         self.csvbutton.destroy()
        #        self.csvbutton=Button(self.root,text='Export CSV',font=('Arial',40),bg='green',borderwidth=5,command=self.csvpressed)     
         #       self.csvbutton.place(x=int(self.x)/2+50,y=int(self.y)-100,width=int(self.y)-230,height=100)
#            elif a=='BubbleGum':
 #               self.csvbutton.destroy()
  #              self.csvbutton=Button(self.root,text='Export CSV',font=('Arial',40),bg='gray',borderwidth=5)     
   #             self.csvbutton.place(x=int(self.x)/2+50,y=int(self.y)-100,width=int(self.y)-230,height=100)
    #        elif a=='House_of_Cards':
     #           self.csvbutton.destroy()
      #          self.csvbutton=Button(self.root,text='Export CSV',font=('Arial',40),bg='gray',borderwidth=5)     
       #         self.csvbutton.place(x=int(self.x)/2+50,y=int(self.y)-100,width=int(self.y)-230,height=100)
        #    elif a=='Lotto':
         #       self.csvbutton.destroy()
          #      self.csvbutton=Button(self.root,text='Export CSV',font=('Arial',40),bg='green',borderwidth=5,command=self.csvpressed)     
           #     self.csvbutton.place(x=int(self.x)/2+50,y=int(self.y)-100,width=int(self.y)-230,height=100)
            #elif a=='SecretSanta':
   #             self.csvbutton.destroy()
    #            self.csvbutton=Button(self.root,text='Export CSV',font=('Arial',40),bg='gray',borderwidth=5)     
     #           self.csvbutton.place(x=int(self.x)/2+50,y=int(self.y)-100,width=int(self.y)-230,height=100)
    def MouseOneDown(self,event):
        if self.pressed==0:
            a=self.var1.get()
            if a=='Marriage':
                self.changer0=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer0.place(y=100,x=int(self.x)-150,width=100,height=50)
                self.changer1=Label(self.root,text='Versuche:',bg='white',font=('Arial',30),borderwidth=1)
                self.changer1.place(y=100,x=int(self.x)-400,width=250,height=50)
                self.csvbutton.destroy()
                self.csvbutton=Button(self.root,text='Export CSV',font=('Arial',40),bg='green',borderwidth=5,command=self.csvpressed)     
                self.csvbutton.place(x=int(self.x)/2+50,y=int(self.y)-100,width=int(self.y)-230,height=100)
            elif a=='Atom':
                self.changer0=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer0.place(y=100,x=int(self.x)-150,width=100,height=50)
                self.changer1=Label(self.root,text='Anzahl der Atome:',bg='white',font=('Arial',30),borderwidth=1)
                self.changer1.place(y=100,x=int(self.x)-600,width=450,height=50)
                self.changer2=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer2.place(y=200,x=int(self.x)-150,width=100,height=50)
                self.changer3=Label(self.root,text='Zerfallswahrscheinlichkeit:',bg='white',font=('Arial',30),borderwidth=1)
                self.changer3.place(y=200,x=int(self.x)-650,width=500,height=50)
                self.csvbutton.destroy()
                self.csvbutton=Button(self.root,text='Export CSV',font=('Arial',40),bg='green',borderwidth=5,command=self.csvpressed)     
                self.csvbutton.place(x=int(self.x)/2+50,y=int(self.y)-100,width=int(self.y)-230,height=100)
            elif a=='BubbleGum':
                self.changer0=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer0.place(y=100,x=int(self.x)-150,width=100,height=50)
                self.changer1=Label(self.root,text='Versuche:',bg='white',font=('Arial',30),borderwidth=1)
                self.changer1.place(y=100,x=int(self.x)-400,width=250,height=50)
                self.csvbutton.destroy()
                self.csvbutton=Button(self.root,text='Export CSV',font=('Arial',40),bg='gray',borderwidth=5)     
                self.csvbutton.place(x=int(self.x)/2+50,y=int(self.y)-100,width=int(self.y)-230,height=100)
            elif a=='House_of_Cards':
                self.changer0=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer0.place(y=100,x=int(self.x)-150,width=100,height=50)
                self.changer1=Label(self.root,text='Versuche:',bg='white',font=('Arial',30),borderwidth=1)
                self.changer1.place(y=100,x=int(self.x)-400,width=250,height=50)
                self.changer2=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer2.place(y=200,x=int(self.x)-150,width=100,height=50)
                self.changer3=Label(self.root,text='Kartenanzahl(32,55):',bg='white',font=('Arial',30),borderwidth=1)
                self.changer3.place(y=200,x=int(self.x)-620,width=450,height=50)
                self.csvbutton.destroy()
                self.csvbutton=Button(self.root,text='Export CSV',font=('Arial',40),bg='gray',borderwidth=5)     
                self.csvbutton.place(x=int(self.x)/2+50,y=int(self.y)-100,width=int(self.y)-230,height=100)
            elif a=='Lotto':
                self.changer0=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer0.place(y=100,x=int(self.x)-150,width=100,height=50)
                self.changer1=Label(self.root,text='Versuche:',bg='white',font=('Arial',30),borderwidth=1)
                self.changer1.place(y=100,x=int(self.x)-400,width=250,height=50)
                self.changer2=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer2.place(y=200,x=int(self.x)-150,width=100,height=50)
                self.changer3=Label(self.root,text='Version:',bg='white',font=('Arial',30),borderwidth=1)
                self.changer3.place(y=200,x=int(self.x)-400,width=250,height=50)
                self.csvbutton.destroy()
                self.csvbutton=Button(self.root,text='Export CSV',font=('Arial',40),bg='green',borderwidth=5,command=self.csvpressed)     
                self.csvbutton.place(x=int(self.x)/2+50,y=int(self.y)-100,width=int(self.y)-230,height=100)
            elif a=='SecretSanta':
                self.changer0=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer0.place(y=100,x=int(self.x)-150,width=100,height=50)
                self.changer1=Label(self.root,text='Versuche:',bg='white',font=('Arial',30),borderwidth=1)
                self.changer1.place(y=100,x=int(self.x)-400,width=250,height=50)
                self.changer2=Text(self.root,bg='white',font=('Arial',30),borderwidth=1)
                self.changer2.place(y=200,x=int(self.x)-150,width=100,height=50)
                self.changer3=Label(self.root,text='Anzahl der Schüler:',bg='white',font=('Arial',30),borderwidth=1)
                self.changer3.place(y=200,x=int(self.x)-550,width=400,height=50)
                self.csvbutton.destroy()
                self.csvbutton=Button(self.root,text='Export CSV',font=('Arial',40),bg='gray',borderwidth=5)     
                self.csvbutton.place(x=int(self.x)/2+50,y=int(self.y)-100,width=int(self.y)-230,height=100)
            self.pressed=1
        else:
            try:
                self.c=self.changer2.get('1.0','end-1c')
                self.changer3.destroy()
                self.changer2.destroy()
            except (AttributeError,TclError):
                    z=0
            try:
                self.b=self.changer0.get('1.0','end-1c')
                self.changer1.destroy()
                self.changer0.destroy()
            except (AttributeError,TclError):
                    z=0
            if self.b=='':
                self.b=1
            else:
                self.b=int(self.b)
            if self.c=='':
                self.c=1
            else:
                self.c=int(float(self.c))
            self.pressed=0
