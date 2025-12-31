# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# Note: Once the chain starts the terms are allowed to go above one milion.

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

