# Project Euler – Problem 1
# Title: Multiples of 3 and 5
# Link: https://projecteuler.net/problem=1

# Find the sum of all natural numbers below a given limit
# that are divisible by 3 or 5.

result = 0

for i in range(1000):
    if i % 5 == 0 or i % 3 == 0:
        result = result + i
print(result)           


    


