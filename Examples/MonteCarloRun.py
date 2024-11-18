from Monte import satCarlo

#set the initial date
initialDate = [2024, 10, 24, 1, 0, 0]


#create variables storing important parameters
sgpUncert = 10 #km
exclusion = 1  #m use 0.1km
interval  = 1  #days
numRuns   = 85
runLength = 2

#create object with initial data
test = satCarlo('Data/tle_data.txt')

#set the parameters
test.setParams(exclusion, sgpUncert)

#run and store the data
results = test.monteRuns(numRuns, runLength, interval, initialDate)

#prints the number of collisions in each run
for result in results:
    print(len(result))