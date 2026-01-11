# Project Euler – Problem 26
# Title: Reciprocal Cycles
# Link: https://projecteuler.net/problem=26
#
# Find the value of d less than a given limit
# for which 1/d has the longest recurring cycle.

max_len = 0
result = 0
for i in range(2, 1000):

    if i % 2 == 0 or i % 5 == 0:
        continue

    remainders = {}
    remainder = 1
    position = 0

    while remainder and remainder not in remainders:
        remainders[remainder] = position
        remainder = (remainder * 10) % i
        position += 1

    cycle_length = position - remainders.get(remainder, position)

    if cycle_length > max_len:
        max_len = cycle_length
        result = i

print("value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part:", result)

