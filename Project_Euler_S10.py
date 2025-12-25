# The sum of the primes below 10 is 2 + 3 + 5 +  7 = 17.
# Find the sum of all the primes below two million.

primes = [2]

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

x = 3
while x < 2000000:
    if is_prime(x):
        primes.append(x)
    x += 1

result = 0
for i in range (len(primes)):
    result = result + primes[i]
print("Sum of all the primes below two million:", result)


