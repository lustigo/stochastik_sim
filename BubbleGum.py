from random import randint

class BubbleGum():
    #You get 5 Trading Cards in a package.
    #The Set has 15 Trading Cards
    #Simulates how often the same trading card is in a package
    #schoolbook p.36/5
    def __init__(self,max):
        self.DEBUG = True #Debug Outputs
        self.cards = [] #which cards i own
        self.double = 0
        self.max=max
        self.happened=0
    def sim(self):
        #simulates, returns self.packs
        #stops when I own all 15 cards
        for x in range(self.max):
            pack = []
            self.double1=self.double
            for _ in range(5):
                card = randint(1,15)
                pack.append(card)
                self.cards.append(card)
            liste=[]
            for c in pack:
                if c in liste:
                    self.double += 1

                else:
                    liste=liste+[c]
            if self.double1!=self.double:
                self.happened+=1
            if self.DEBUG:
                print(pack)
                print(self.double)

    def getrel(self):
        #returns how many double cards in one pack at the first 5 packs
        return (self.double/self.max,self.happened/self.max)


