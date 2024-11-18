import sgp4.api as sgp
import random

#Sattelite class allows sats to be grouped together and retain basic info
class sat:
    #Basic Var inits
    def __init__(self, name, line1, line2):
        self.name = name
        self.line1 = line1
        self.line2 = line2
    
    #getState function returns [position, velocity] at given date in the True Equator Mean Equinox (TEME) Reference Frame
    def updateState(self, initialDate, day, posUncert):
    
        satellite = sgp.Satrec.twoline2rv(self.line1, self.line2)
        
        #Convert the calendar date to Julian Date
        jd, fr = sgp.jday(initialDate[0], initialDate[1], initialDate[2] + day, initialDate[3], initialDate[4], initialDate[5])
        
        #Get the satellite's position and velocity at the specified time
        e, r, v = satellite.sgp4(jd, fr)
        
        if e == 0:
            #generating uncertainty for each run:
            xRand = random.random() * 2 * posUncert - posUncert
            yRand = random.random() * 2 * posUncert - posUncert
            zRand = random.random() * 2 * posUncert - posUncert
            
            self.pos = (r[0] + xRand, r[1] + yRand, r[2] + zRand)
            self.vel = v
            return 1
        else:
            return 0

#parseSats function generates and returns a sattlite list from the given data, assuming the twoline format with names
def parseSats(fileName):
    file = open(fileName, 'r')
    print("Parsing Sats")
    
    satList = []
    lines = []
    
    print("reading lines")
    for line in file:
        lines.append(line)
    
    print("generating sattelite list")
    for i in range(0, len(lines), 3):
        satList.append(sat(lines[i], lines[i+1], lines[i+2]))
    
    return satList
