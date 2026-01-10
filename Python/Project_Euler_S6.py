# Project Euler – Problem 6
# Title: Sum Square Difference
# Link: https://projecteuler.net/problem=6
#
# Find the difference between the square of the sum
# and the sum of the squares of the first n natural numbers.

x = 0
y = 0
for i in range(1,101):
    x = i**2
    y = x + y

a = 0
for k in range(1,101):
    a = a + k
b = a**2

result = b - y
print("Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum:", result)

