# Project Euler – Problem 21
# Title: Amicable Numbers
# Link: https://projecteuler.net/problem=21
#
# Find the sum of all amicable numbers
# under a given limit.

def sum_of_divs(n):
    divs = []
    sum_divs = 0
    for i in range(1, n):
        if n % i == 0:
            divs.append(i)
            sum_divs = sum(divs)
    return sum_divs

x = 0
y = 0
z = 0
amicable_num = []
while x < 10000:
    x += 1
    y = sum_of_divs(x)
    z = sum_of_divs(y)
    if x == z and x != y:
        amicable_num.append(x)

print("Sum of all the amicable numbers under 10000:", sum(amicable_num))


