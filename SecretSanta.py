from random import shuffle
class SecretSanta():
    #simulates "Secret Santa" and generates a probability value for getting the own name
    # schoolbook p.36/6
    def __init__(self,max,size):
        self.max = max #how often should be drawn?
        self.size = size #how many students are in the class?
        self.students = list(range(size))
        self.me = 0 #amount how often a student has drawn himself
        self.turns = [] #all turns
        self.DEBUG = True #Debug Console Output

    def sim(self):
        #simulates and returns self.me
        for _ in range(self.max):
            cards = list(self.students) #Papers which will be drawn by students
            shuffle(cards)
            x = 0
            turn = []
            for y in cards:
                if x == y:
                    self.me+=1
                turn.append(str(x) + "-" + str(y))
                x+=1
            if self.DEBUG:
                print(turn)
                print(self.me)
            self.turns.append(turn)
        return self.me

    def getrel(self):
        #returns relative how often somebody has drawn himself
        return self.me/self.max/self.size

