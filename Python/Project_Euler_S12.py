# Project Euler – Problem 12
# Title: Highly Divisible Triangular Number
# Link: https://projecteuler.net/problem=12
#
# Find the first triangular number
# that has over a given number of divisors.

tri_num = [1, 3, 6]
divisors = []

def is_500_divs(n):
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

a = 4
b = 6
while len(divisors) < 501:
    divisors.clear()
    b = b + a
    tri_num.append(b)
    a += 1
    is_500_divs(max(tri_num))

print("The value of the first triangle number to have over five hundred divisors: ", max(tri_num))
divisors.sort()
print("Total divisors: ", divisors)

