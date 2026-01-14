// Project Euler – Problem 5
// Title: Smallest Multiple
// Link: https://projecteuler.net/problem=5
//
// Find the smallest positive number that is evenly divisible
// by all numbers from 1 to n.

#include <stdio.h>

long long gcd(long long a, long long b)
{
    while (b != 0)
    {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

long long lcm(long long a, long long b)
{
    return (a * b) / gcd(a, b);
}

int main()
{
    long long result = 1;

    for (int i = 1; i <= 20; i++)
    {
        result = lcm(result, i);
    }

    printf("Smallest multiple: %lld\n", result);
    return 0;
}
