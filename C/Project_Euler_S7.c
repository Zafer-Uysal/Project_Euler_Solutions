// Project Euler – Problem 7
// Title: 10001st Prime
// Link: https://projecteuler.net/problem=7
//
// Find the nth prime number.

#include <stdio.h>

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

long long count = 0; 
int x  = 0;
while (count <= 10000)
{
    x++;
    if (is_prime(x))
    {
        count++;
    }
}

printf("10001st prime: %d" , x);
}