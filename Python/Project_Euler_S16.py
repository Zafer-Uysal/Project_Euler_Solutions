# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

x = 2 ** 1000 
result = 0

for i in str(x):
    result = result + int(i)

print("Sum of the digits of the number 2^1000: ", result)
