from random import random

class Atom():
    #Simulates radioactive Atoms (Bernoulli)
    #https://www.lernhelfer.de/schuelerlexikon/mathematik-abitur/artikel/simulation
    #At each tick the atom spontaneously decays (probability p)

    def __init__(self,p,n):
        self.p = p #probability if atom decays
        self.n = n #how many atoms we have?
        self.DEBUG = True #Debug Console Output
        self.amount = [self.n] #list how many atoms are alive after each tick

    def sim(self):
        #simulates and returns self.amount
        amount = self.n
        while not amount ==0:
            am = amount
            if self.DEBUG:
                print("amount: " + str(amount))
            for _ in range(am):
                if random() <= self.p:
                    amount -= 1
            self.amount.append(amount)
        return self.amount

    def writefile(self, filename, output):
        #writes output in filename and returns True
        file = open(filename, 'w')
        file.write(output)
        file.close()
        return True

    def exportCSV(self, filename):
        output = "Tick, Amount \n"
        n = 0
        for a in self.amount:
            output+= str(n)+","+str(a)+"\n"
            n += 1
        return self.writefile(filename, output)