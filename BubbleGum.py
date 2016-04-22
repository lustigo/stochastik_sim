from random import randint

class BubbleGum():
    #You get 5 Trading Cards in a package.
    #The Set has 15 Trading Cards
    #Simulates how often the same trading card is in a package
    #schoolbook p.36/5
    def __init__(self):
        self.DEBUG = True #Debug Outputs
        self.cards = [] #which cards i own
        self.double = 0

    def sim(self):
        #simulates, returns self.packs
        #stops when I own all 15 cards
        p = 1
        while p <= 5:
            pack = []

            for _ in range(5):
                card = randint(1,15)
                pack.append(card)
                self.cards.append(card)

            for c in pack:
                if pack.count(c) >= 2:
                    self.double += 1

            if self.DEBUG:
                print(pack)
                print(self.double)
            p+=1
        while not set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]).issubset(self.cards):
            for _ in range(5):
                self.cards.append(randint(1,15))
        if self.DEBUG:
            print(self.cards)
        return self.cards

    def getrel(self):
        #returns how many double cards in one pack at the first 5 packs
        return b.double/25
    def getpacks(self):
        #returns how many packs I own
        return len(b.cards)/5





