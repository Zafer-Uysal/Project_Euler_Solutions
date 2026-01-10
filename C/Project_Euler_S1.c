// Project Euler – Problem 1
// itle: Multiples of 3 and 5
// Link: https://projecteuler.net/problem=1

// Find the sum of all natural numbers below a given limit
// that are divisible by 3 or 5.

#include <stdio.h>

int main()
{
int result = 0;
int i;

for (i = 0;  i < 1000; i++)
{
    if (i % 5 == 0 || i % 3 == 0)
    {
        result = result + i;
    }
}

printf("%d", result);
}
