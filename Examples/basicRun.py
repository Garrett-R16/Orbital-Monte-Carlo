from Monte import satCarlo

#Set the initial date
initialDate = [2024, 10, 24, 1, 0, 0]

#Create Carlo object with TLE Data
test = satCarlo('Data/tle_data.txt')

#Set the parameters
test.setParams(1, 5)

#Run and store the results
results = test.run(3, 1, initialDate)

#Print the length, will give the number of collisions
print(len(results))

#print the names of sats in collisions
for result in results:
    print(result[0].name)
    print(result[1].name)