from random import shuffle
class Lotto():
    #Simulates a TV-Show: 18 Lotterie balls in a list
    #6 different names, balls pop out, first name who was drawn 3 times wins a handshake
    #schoolbook p.37/8
    #How is the probability, that a winner is drawn, but another players name was not drawn yet
    #c) 4:x-fach Wurf möglich

    def __init__(self,max):
        self.max = max #How often should be played?
        self.DEBUG = True #Debug Console Outputs
        self.balls = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5] # all lottery balls
        self.turns = [] # which where drawn?

    def sim(self):
        #simulates and returns drawn balls
        for _ in range(self.max):
            drawn = []
            turn = list(self.balls)
            shuffle(turn)
            o = True
            while o:
                p = turn.pop()
                drawn.append(p)
                if len(turn) == 0:
                    o = False
                else:
                    o = not self.iswinner(drawn)
            if self.DEBUG:
                print(drawn)
            self.turns.append(drawn)

    def exportCSV(self,filename):
        #exports Data to CSV
        #shows how the probability changes
        #rounded to 4 digits
        output = "Round, Probability\n"
        x = 1
        count = 0
        for draw in self.turns:
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
            output+=str(x)+","+str(round(count/x,4))+"\n"
            x += 1
        return self.writefile(filename,output)

    def getrel(self):
        #returns how the probability is, that a winner is drawn, but another players name was not drawn yet
        count = 0
        for draw in self.turns:
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
        return count/len(self.turns)

    def iswinner(self, draw):
        #returns if sb. has already won
        if draw.count(0) == 3:
            return True
        elif draw.count(1) == 3:
            return True
        elif draw.count(2) == 3:
            return True
        elif draw.count(3) == 3:
            return True
        elif draw.count(4) == 3:
            return True
        elif draw.count(5) == 3:
            return True
        else:
            return False

    def writefile(self, filename, output):
        #writes output in filename and returns True
        file = open(filename, 'w')
        file.write(output)
        file.close()
        return True
