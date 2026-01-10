# Project Euler – Problem 5
# Title: Smallest Multiple
# Link: https://projecteuler.net/problem=5
#
# Find the smallest positive number that is evenly divisible
# by all numbers from 1 to n.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

result = 1
for i in range(1, 21, 1):
    result = lcm(result, i)

print("Smallest positive number that is evenly divisible by all of the numbers from 1 to 20:", result)