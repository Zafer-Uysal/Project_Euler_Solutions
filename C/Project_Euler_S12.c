// Project Euler – Problem 12
// Title: Highly Divisible Triangular Number
// Link: https://projecteuler.net/problem=12
//
// Find the first triangular number
// that has over a given number of divisors.

#include <stdio.h>
#include "math.h"

long long is_500_divs(int n)
    {
        int counter = 0;
        for (int i = 1; i < ((int)sqrt(n) + 1); i++)
        {
            if (n % i == 0)
            {
                counter++;
                int y = n / i;
                if (i != y)
                {
                    counter++;
                }
            }  
        }
        return counter;
    }

int main()
{
    long long a = 4;
    long long b = 6;
    long long result = 0;

    while (1)
    {
        b += a;
        a++;
        int count = is_500_divs(b);
        if (count > 500)
        {
                printf("First triangular number that has over 500 divisors: %lld", b);
                break;
        }
    }
    return 0;
}




