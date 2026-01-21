// Project Euler – Problem 14
// Title: Longest Collatz Sequence
// Link: https://projecteuler.net/problem=14
//
// Find the starting number under a given limit
// that produces the longest Collatz sequence.

#include <stdio.h>

int main()
{
    int max_len = 0;
    long long max_num = 0;
    for (int i = 3; i < 1000000; i += 2)
    {
        long long n = i;
        int chain_len = 0;
        while (n != 1)
        {
            if ((n % 2) == 0)
            {
                n /= 2;
            }
            else
            {
                n = (3 * n) + 1;
            }
            chain_len++;
        }
        
        if (chain_len > max_len)
        {
            max_len = chain_len;
            max_num = i;
        }
    }
    printf("Starting number under 1000000 that produces the longest Collatz sequence: %lld", max_num);
    return 0;
}




