// Project Euler – Problem 10
// Title: Summation of Primes
// Link: https://projecteuler.net/problem=10
//
// Find the sum of all prime numbers below a given limit.

#include <stdio.h>
#include <stdbool.h>

bool is_prime(int a)
{
    if (a <= 1)
    {    
        return false;
    }
    else if (a == 2)
    {    
        return true;
    }
    else if (a % 2 == 0)
    {  
        return false;
    }

    for (int i = 3; i * i <= a; i += 2)
        {
            if (a % i == 0)
            {
                return false;
            }
        }
    return true;
}

int main()
{
    int x = 2;
    long long result = 0;
    while (x < 2000000)
    {
        if (is_prime(x))
        {
            result += x;
        }
        x++;
    }
    printf("Sum of all prime numbers below two million: %lld", result);
    
    return 0;
}
