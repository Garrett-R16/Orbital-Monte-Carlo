# Monte Carlo Simulations for Orbital Modeling

This repo contains information on how to use the Monte Carlo Simulation I made for [Viasat](https://www.viasat.com/) as a part of [The Data Mine](https://datamine.purdue.edu/) to analyze Satellites in orbit. Let's begin with:

## The Data

The Data should be in the format of TLE data. See the data folder for an [example of what that should look like](https://github.com/Garrett-R16/Orbital-Monte-Carlo/blob/main/Data/tle_format_example.txt).

## How to use it

### Initializing the Object and Setting up Simulations

The main file contains a satCarlo class, which can be initialized with the path to your data file:

``` Ruby
carloObj = satCarlo("tleData.txt")
```

Once this is done, you should also set up your simulation parameters. There are two main parameters to choose: the exclusion zone, which is the keepout zone for each satellite, in km, and the position uncertainty, which is the uncertainty in position for each satellite.

``` Ruby
posUncert = 10 #km
exclusion = 1  #km

carloObj.setParams(exclusion, posUncert)
```

### Performing Simulations

Once your Monte Carlo object is initialized, you can begin performing runs.

#### Standalone Runs

If you want to perform a single run of a specified length and interval, you can call the run function. The length is the duration, in days, and the interval is the step time of the simulation, also in days. This function will return an array where each member is an array containing the two satellite objects that collided. You also need the initial moment you want to propagate from, in the form of [year, month, day, hour, minute, second].

``` Ruby
length   = 365 #days
interval = 1   #days
initialDate = [2024, 10, 24, 1, 0, 0]

results = carloObj.run(3, 1, initialDate)
```

#### Multiple Runs (Monte Carlo)
If you want to perform a multiple runs of a specified length and interval, you can call the run function. The length is the duration, in days, and the interval is the step time of the simulation, also in days. This function will return an array where each member is a run array where each member is an array containing the two satellite objects that collided. You also need the initial moment you want to propagate from, in the form of [year, month, day, hour, minute, second].

``` Ruby
length   = 365 #days
interval = 1   #days
runNum   = 20  #runs
initialDate = [2024, 10, 24, 1, 0, 0]

results = carloObj.monteRuns(numRuns, runLength, interval, initialDate)
```

#### Analyzing the data

When analyzing the specific satellites engaged in collisions, some useful parameters you can look at are:

``` Ruby
currentSat.name #returns the name of the sat
currentSat.pos  #returns the position of the sat as a 3 axis vector, in the True Equator Mean Equinox (TEME) Reference Frame
currentSat.vel  #returns the velocity of the sat as a 3 axis vector, in the TEME Reference Frame
```

## Examples

Checkout [the examples folder](https://github.com/Garrett-R16/Orbital-Monte-Carlo/tree/main/Examples) for some examples on how I've set up some simulations. Some interesting statistics from stuff I've set up are:

When using a run length of 365 days, an interval of 5 days, a position uncertainty of 10 km, the same initial date and the number of runs as 85, as above I got the probability of a collision in the next year to be 2.35%. When using the same parameters, but with an exclusion zone of 1 km, a run length of 2 days, and an interval of 1 day, I got the probability of a collision in the next 2 days to be 71.8%.

Keep in mind, the exclusion zones in these simulations aren't realistic to assume sattelites colliding, a more realistic number to use for that case would be 0.01 km (or 10m). These are just examples of some results generated from me experimenting with parameters.

## The Next Steps

- Making the code more efficient
- Adding debris generation
- Data analysis tools
- Machine Learning aspect (?)
