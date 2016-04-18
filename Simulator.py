class Simulator():
    #does background work, calculates simulations
    #def __init__(self):

    def exportCSV(self,list,path):
        #writes a CSV-file of the list to path
        ls = map(str,list)
        txt = "\n".join(ls)
        file = open(path, 'w')
        file.write(txt)
        file.close()
        return True
