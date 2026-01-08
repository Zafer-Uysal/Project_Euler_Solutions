# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
# the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis 
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def is_abundant(n):
    div_sum = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            div_sum += i
            if i != 1 and i != n // i:
                div_sum += n // i
    return div_sum > n

abundant_nums = []
for i in range(12, 28123):
    if is_abundant(i):
        abundant_nums.append(i)

sum_abundant = [False] * 28123
for i in range(0, len(abundant_nums)):
    for j in range(i, len(abundant_nums)):
        x = abundant_nums[i] + abundant_nums[j]
        if x < 28123:
            sum_abundant[x] = True
        else:
            break

result = 0
for i in range(0, 28123):
    if not sum_abundant[i]:
        result += i

print("Sum of all the positive integers which cannot be written as the sum of two abundant numbers:", result)
