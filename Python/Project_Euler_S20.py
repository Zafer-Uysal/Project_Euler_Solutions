# Project Euler – Problem 20
# Title: Factorial Digit Sum
# Link: https://projecteuler.net/problem=20
#
# Find the sum of the digits of n factorial.

result = 1
for n in range(1,101):
     result *= n

resultl= []
for i in str(result):
    resultl.append(int(i))
     
print(sum(resultl))     
