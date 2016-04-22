from random import shuffle


class Marriage():
    # Simulation by Bernoulli
    # simulates how many marriages break if at a specific time 10 of 20 people die
    # schoolbook p.32

    def __init__(self):
        self.complete = [] #List of all rounds
        self.marriages = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,0,0] # all 20 persons in 10 marriages
        self.run = False #checks if simulation is finished
        self.DEBUG = True #if True, console output of single turn list
        if self.DEBUG:
            print(self.marriages)

    def sim(self, max):
        # simulates "Marriage"
        # takes how often the simulation should run, returns the complete list of turns
        if not self.run:
            for _ in range(max - 1):
                m = list(self.marriages)
                shuffle(m)
                if self.DEBUG:
                    print ("Shuffel:")
                    print (m)
                if self.DEBUG:
                    print ("Alive:")
                    print (m[:10])
                self.complete.append(m[:10])
            self.run = True
            return self.complete

    def exportcsv(self, filename):
        #exports CSV: first column round number, second column amount of complete pairs
        #rel rounded to 0.0000
        #avg rounded to 0.00
        i = 1
        output = "Total:,5x,4x,3x,2x,1x,0x\n,"
        for p in self.gettotal():
            output+= str(p) +","
        output+="\n Relative:\n,"
        for o in self.getrel():
            output+= str(round(o,5))+","
        output+="\n Average:, " + str(round(self.getavg(),2)) + "\n\n Single Turns: \n #,Amount of complete pairs\n"
        for x in self.complete:
            output += str(i)+","
            output += str(self.countpairs(x))+"\n"
            i += 1
        #output = output.replace(".",",")
        self.writefile(filename,output)
        return True


    def countpairs(self,turn):
        #returns amount of complete pairs in turn
        count = 0
        if self.iscomplete(turn,0):
            count += 1
        if self.iscomplete(turn,1):
            count += 1
        if self.iscomplete(turn,2):
            count += 1
        if self.iscomplete(turn,3):
            count += 1
        if self.iscomplete(turn,4):
            count += 1
        if self.iscomplete(turn,5):
            count += 1
        if self.iscomplete(turn,6):
            count += 1
        if self.iscomplete(turn,7):
            count += 1
        if self.iscomplete(turn,8):
            count += 1
        if self.iscomplete(turn,9):
            count += 1
        return count

    def iscomplete(self, turn, pair):
        #returns if a marriage is complete in that turn
        return turn.count(pair) == 2

    def writefile(self, filename, output):
        #writes output in filename and returns True
        file = open(filename, 'w')
        file.write(output)
        file.close()
        return True

    def getavg(self):
        #returns average amount of complete marriages
        sum = 0
        for x in self.complete:
            sum += self.countpairs(x)
        return sum/len(self.complete)

    def getrel(self):
        #returns relativity in list (how often are 5 pairs alive, 4 pairs ...)
        sum = self.gettotal()
        l = len(self.complete)
        newsum = []
        newsum.append(sum[0]/l)
        newsum.append(sum[1]/l)
        newsum.append(sum[2]/l)
        newsum.append(sum[3]/l)
        newsum.append(sum[4]/l)
        newsum.append(sum[5]/l)
        return newsum

    def gettotal(self):
        #returns absolute in list (how often are 5 pairs alive, 4 pairs ...)
        five = 0
        four = 0
        three = 0
        two = 0
        one = 0
        zero = 0
        for x in self.complete:
            p = self.countpairs(x)
            if p == 0:
                zero += 1
            elif p == 1:
                one += 1
            elif p ==2:
                two +=1
            elif p == 3:
                three += 1
            elif p == 4:
                four += 1
            else:
                five += 1
        return [five, four, three, two, one, zero]


