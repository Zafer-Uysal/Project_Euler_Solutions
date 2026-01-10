# Project Euler – Problem 9
# Title: Special Pythagorean Triplet
# Link: https://projecteuler.net/problem=9
#
# Find the Pythagorean triplet for which
# a + b + c equals a given value.


for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a:", a, "b:", b, "c:", c)
            print("Product of abc:", a * b * c)





