# Project Euler – Problem 16
# Title: Power Digit Sum
# Link: https://projecteuler.net/problem=16
#
# Find the sum of the digits of a number
# raised to a given power.

x = 2 ** 1000 
result = 0

for i in str(x):
    result = result + int(i)

print("Sum of the digits of the number 2^1000: ", result)
