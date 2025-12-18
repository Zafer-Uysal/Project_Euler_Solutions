# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the given 600851475143

start_num = 600851475143
prime_factors = []
i = 2

while i <= start_num:
    while start_num % i == 0:
        prime_factors.append(i)
        start_num /= i
    i += 1

print(max(prime_factors))





    


