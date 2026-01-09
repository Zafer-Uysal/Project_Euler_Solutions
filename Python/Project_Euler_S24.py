# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

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


