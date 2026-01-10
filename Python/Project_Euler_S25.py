# Project Euler – Problem 25
# Title: 1000-Digit Fibonacci Number
# Link: https://projecteuler.net/problem=25
#
# Find the index of the first Fibonacci number
# with a given number of digits.

fibonacci = [1, 1, 2]

while len(str(fibonacci[-1])) < 1000:
    new_value = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(new_value)

print("Index of the first term in the Fibonacci sequence to contain 1000 digits:", fibonacci.index(fibonacci[-1]) + 1)
