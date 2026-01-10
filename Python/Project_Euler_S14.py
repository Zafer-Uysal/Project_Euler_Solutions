# Project Euler – Problem 14
# Title: Longest Collatz Sequence
# Link: https://projecteuler.net/problem=14
#
# Find the starting number under a given limit
# that produces the longest Collatz sequence.

chain = []
chain_len = []
start_num = []

for i in range(1, 1000000, 2):
    start_num.append(i)
    while i != 1:
        if i % 2 == 0:
            chain.append(i)
            i /= 2 
        else:
            chain.append(i)
            i = (3 * i) + 1
    chain.append(i)
    chain_len.append(len(chain))
    chain.clear()

print("Longest chain lenght: ", max(chain_len))
longest_chain_index = chain_len.index(max(chain_len))
print("Longest chain under one million started with: ", start_num[longest_chain_index])

