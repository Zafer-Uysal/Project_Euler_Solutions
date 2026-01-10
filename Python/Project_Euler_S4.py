# Project Euler – Problem 4
# Title: Largest Palindrome Product
# Link: https://projecteuler.net/problem=4
#
# Find the largest palindrome made from the product
# of two n-digit numbers.

x = 100
y = 100
palindromes = []

def palindrome(a):
    for i in range(len(str(a))):
            if i in (0, 1, 2):
                ftd = str(a)[0] + str(a)[1] + str(a)[2]
            elif i in (3, 4, 5):
                ltd = str(a)[-1] + str(a)[-2] + str(a)[-3]
    if  ftd == ltd:
            palindromes.append(a)  

while x <= 999 and y <= 999:
    for k in range(100,1000,1):
        palindrome(x * y)
        x += 1
        if x == 999:
             y += 1
             x = 100
print("Largest palindrome made from the product of two 3-digit numbers:", max(palindromes))




