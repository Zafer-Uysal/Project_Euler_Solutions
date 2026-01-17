// Project Euler – Problem 9
// Title: Special Pythagorean Triplet
// Link: https://projecteuler.net/problem=9
//
// Find the Pythagorean triplet for which
// a + b + c equals a given value.

#include <stdio.h>

int main()
{
    for (int a = 1; a < 1000; a++)
    {
        for (int b = a + 1; b < 1000; b++)
        {
            int c = 1000 - a - b;
            if ((a*a) + (b*b) == c*c)
            {
                printf("a: %d b: %d c: %d \n", a, b, c);
                printf("Product of abc: %d", a*b*c);
            }
        }
    }
    return 0;
}

