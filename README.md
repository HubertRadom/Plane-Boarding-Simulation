Project for University Course

The goal of the project was to simulate and compare different strategies for boarding a plane. In order to do it, we created a simplified model of a plane with 96 seats.  The plane has 16 rows with 6 seats in each and corridor is 1 patch wide. If not specified, simulations are performed with seat shuffling enabled and stowing time drawn from a normal distribution with mean equal to 5 ticks and standard deviation equal to 1 tick. Simulation is finished when all passengers reach their seats. For each seating strategy, 100 simulations are performed. At the end mean is calculated and a histogram is drawn. 
Comparing results allowed us to answer for few questions like "How long would the bag stowing need to take for the seat shuffles to cause more delay than the stowing?" and more.

To <b>start</b> the simulation run main.py file.
If you want to see the visualization, set VISUALIZE value (in main.py) as True. 
