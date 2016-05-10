from random import randint

class Coins(object):

    #p.37/9

    def __init__(self,max):
        self.max = max # amount of tries
        self.wuerfe = [] # list of coins 

    def sim(self):
        #simuliert
        for x in range(self.max):
            self.wuerfe.append(str(randint(1,2)))

    def geterg(self):
        #return absoulute as list
        x = 0
        www = 0 #combination head head head
        zwz = 0 # combination number head number
        for c in self.wuerfe:
            l = []
            if x < len(self.wuerfe) - 2:
                l.append(c)
                l.append(self.wuerfe[x+1])
                l.append(self.wuerfe[x+2])
                x += 1
                if "".join(l) == "111":
                    www += 1
                elif "".join(l) == "212":
                    zwz += 1
        erg = [www,zwz]
        return erg

    def getrel(self):
        # return relative as list
        e = self.geterg()
        r = [e[0]/self.max,e[1]/self.max]
        return r 
        
            
