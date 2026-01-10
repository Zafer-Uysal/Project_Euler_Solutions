# Project Euler – Problem 7
# Title: 10001st Prime
# Link: https://projecteuler.net/problem=7
#
# Find the nth prime number.

def is_prime(a):
    if a <= 1:
        return False
    
    elif a == 2:
        return True

    elif a % 2 == 0:
        return False
    
    for i in range(3, int(a**0.5) + 2):
        if a % i == 0:
            return False
        
    return True

primes = [2]
x = 3
while len(primes) <= 10000:
    if is_prime(x):
        primes.append(x)
    x += 2

print(len(primes),"st prime" , primes[-1])