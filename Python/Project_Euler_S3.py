# Project Euler – Problem 3
# Title: Largest Prime Factor
# Link: https://projecteuler.net/problem=3
#
# Find the largest prime factor of a given number.

start_num = 600851475143
prime_factors = []
i = 2

while i <= start_num:
    while start_num % i == 0:
        prime_factors.append(i)
        start_num /= i
    i += 1

print(max(prime_factors))





    


