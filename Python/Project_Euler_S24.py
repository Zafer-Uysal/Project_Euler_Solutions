# Project Euler – Problem 24
# Title: Lexicographic Permutations
# Link: https://projecteuler.net/problem=24
#
# Find the nth lexicographic permutation
# of a set of digits.

def per(per_list):
    if len(per_list) == 1:
        return [per_list]

    result = []
    for i in range(len(per_list)):
        select = per_list[i]
        left = per_list[:i] + per_list[i+1:]

        for j in per(left):
            result.append([select] + j)
            if len(result) == 1000000:
                return result
                
    return result

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perm_list = per(nums)

print("Millionth lexicographic permutation of the digits:", perm_list[999999])


