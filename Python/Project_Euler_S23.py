# Project Euler – Problem 23
# Title: Non-Abundant Sums
# Link: https://projecteuler.net/problem=23
#
# Find the sum of all positive integers
# that cannot be written as the sum of two abundant numbers.

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
