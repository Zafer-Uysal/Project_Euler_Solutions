# Project Euler – Problem 2
# Title: Even Fibonacci Numbers
# Link: https://projecteuler.net/problem=2
#
# Find the sum of even-valued Fibonacci terms
# whose values do not exceed a given limit.

fib_sum = 0
fibonacci = [1,2]

while fibonacci[-1] < 4000000:
    new_value = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(new_value)

for i in range(len(fibonacci) - 1):
    if fibonacci[i] % 2 == 0:
        fib_sum = fib_sum + fibonacci[i]

print(fib_sum)



    


