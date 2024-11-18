from lib.Satellite import parseSats

#Sat carlo class allows you to create a Carlo object, which has an array containing the data.
#You can set up different simulations with different lengths, number of runs, and and parameters
#The initial date has to be in an array of the form: [year, month, day, hour, minute, second]
class satCarlo:
    #init function, pass in file name
    def __init__(self, fileName):
        self.sats = parseSats(fileName)

    #Exclusion, in km, and position uncertainty, in km
    def setParams(self, exclusion, posUncert):
        self.exclusion = exclusion
        self.posUncert = posUncert
        
    #propagate from given date by x days
    def propagate(self, date, day):
        i = 0
        satsLength = len(self.sats)
        print("propagating sats")
        
        while(i < satsLength):
            e = self.sats[i].updateState(date, day, self.posUncert)

            if e == 0:
                del self.sats[i]
                satsLength -= 1
                continue
            
            i += 1
    
    #perform a run of a specified length and interval, given an initial date
    def run(self, length, interval, initialDate):
        day = 0
        
        collisions = []
        
        while day < length:
            print(f"Running Day {day + 1}")
            
            self.propagate(initialDate, day)
            satNum = len(self.sats)
            
            print("Finding collisions")
            for i in range(0, satNum):
                sat1 = self.sats[i]
                
                for j in range(i + 1, satNum):
                    sat2 = self.sats[j]
                    
                    if checkCollision(self.exclusion, sat1.pos, sat2.pos):
                        print("collision detected")
                        collisions.append((sat1, sat2, day))
            
            day += interval
        
        return collisions
    
    #perform a set amount of runs of a specified length and interval, given an initial date
    def monteRuns(self, numRuns, length, interval, initialDate):
        monteArray = []
        
        runPos = 0
        while runPos < numRuns:
            print(f"On run {runPos + 1}")
            monteArray.append(self.run(length, interval, initialDate))
            runPos += 1
        
        return monteArray

#basic collision checking function assuming the exclusion zone is a square with a specified length
def checkCollision(exclusion, p1, p2):
    return abs(p1[0] - p2[0]) < exclusion and abs(p1[1] - p2[1]) < exclusion and abs(p1[2] - p2[2]) < exclusion