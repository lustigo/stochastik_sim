from random import shuffle,randint
class House_of_Cards():
    #Simulates two decks of 12(32,55) cards, which will be drawn at the same time
    #calculates how often two similar cards will be drawn at the same time
    #forgive me the joke of the class name -> uncreative
    #schoolbook p.33/2
    #b) bei Würfeln wird gezogener Wert nich entfernt

    def __init__(self, max, i=None):
        self.max = max #how often should be drawn?
        self.card_amount = i #How many cards are in the decks? # 12 is default
        self.double = 0 #How often was the same card drawn?
        self.DEBUG = True #Debug Console Outputs

    def sim(self):
        #simulates and returns self.double
        self.double = 0
        for _ in range(self.max):
            deck1 = list(range(self.card_amount))
            shuffle(deck1)
            deck2 = list(range(self.card_amount))
            shuffle(deck2)
            while len(deck1)>0:
                if self.DEBUG:
                    print ("DECK1:")
                    print (deck1)
                    print ("DECK2:")
                    print (deck2)
                if deck1.pop() == deck2.pop():
                    self.double +=1
                    if self.DEBUG:
                        print (self.double)
        return self.double

    def getrel(self):
        #returns relative how often the same card was drawn
        return self.double/self.max#/self.card_amount

    def sim_dodekaeder(self):
        #simulates two twelve side cubes thrown at the same time
        #returns self.double
        self.double = 0
        for _ in range(self.max):
            for _ in range(self.card_amount):
                c1 = randint(1,self.card_amount)
                c2 = randint(1,self.card_amount)
                if self.DEBUG:
                    print("c1: " + str(c1) + " c2: "+str(c2))
                if c1== c2:
                    self.double += 1
        return self.double
