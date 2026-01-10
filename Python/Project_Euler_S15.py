# Project Euler – Problem 15
# Title: Lattice Paths
# Link: https://projecteuler.net/problem=15
#
# Find the number of routes through a grid
# moving only right and down.

import math

result = math.comb(40, 20)
print("Possible routes are there through a 20x20 grid: ", result)
