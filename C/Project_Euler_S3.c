// Project Euler – Problem 3
// Title: Largest Prime Factor
// Link: https://projecteuler.net/problem=3
//
// Find the largest prime factor of a given number.

#include <stdio.h>

long long start_num = 600851475143;
int i = 2;
int result = 0;

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

    for (int i = 3; i * i <= a + 2; i += 2)
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

while (i <= start_num)
{
    while (start_num % i == 0)
    {
        if (is_prime(i))
        {
            result = i;
        }
        start_num /= i;
    }
    i += 1;
}

printf("Largest prime factor of 600851475143: %d", result);
}

