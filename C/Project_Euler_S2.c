// Project Euler – Problem 2
// Title: Even Fibonacci Numbers
// Link: https://projecteuler.net/problem=2
//
// Find the sum of even-valued Fibonacci terms
// whose values do not exceed a given limit.

#include <stdio.h>

int main()
{
    int a = 1;
    int b = 2;
    int sum = 0;
    int next = 0;

    while (b <= 4000000)
    {
        if (b % 2 == 0)
        {
            sum += b;
        }

        next = a + b;
        a = b;
        b = next;
    }

    printf("Sum of even-valued Fibonacci terms whose values do not exceed 4000000: %d\n", sum);
    return 0;
}
