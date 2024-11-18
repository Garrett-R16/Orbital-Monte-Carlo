## Monte Carlo Simulations for Orbital Modeling

This repo contains information on how to use the Monte Carlo Simulation I made to analyze Satellites in orbit. Let's begin with:

# The Data

The Data should be in the format of TLE data. See the data folder for an example of what that should look like.

# How to use it

The main file contains a satCarlo class, which can be initialized with the path to your data file:

``` Ruby
carloObj = satCarlo("tleData.txt")
```
