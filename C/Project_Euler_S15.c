// Project Euler – Problem 15
// Title: Lattice Paths
// Link: https://projecteuler.net/problem=15
//
// Find the number of routes through a grid
// moving only right and down.

#include <stdio.h>

long long factorial(int n)
{
    long long
     result = 1;
    for (int i = 1; i <= n; i++)
    {
        result *= i;
    }

    return result;
}

long long combination(int n, int r)
{
    if (r > n - r)
        r = n - r;

    long long result = 1;

    for (int i = 1; i <= r; i++)
    {
        result = result * (n - r + i) / i;
    }

    return result;
}

long long path_num = 0;
int main()
{
    path_num = combination(40, 20);
    printf("Possible routes are there through a 20x20 grid: %lld", path_num);
    return 0;
}

