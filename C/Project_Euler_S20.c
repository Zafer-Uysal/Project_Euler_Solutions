// Project Euler – Problem 20
// Title: Factorial Digit Sum
// Link: https://projecteuler.net/problem=20
//
// Find the sum of the digits of n factorial.

#include <stdio.h>

int main()
{
    int digits[200] = {0}; 
    digits[0] = 1;

    int size = 1;

    for (int i = 2; i <= 100; i++)
    {
        int carry = 0;
        for (int j = 0; j < size; j++)
        {
            int prod = digits[j] * i + carry;
            digits[j] = prod % 10;
            carry = prod / 10;
        }

        while (carry > 0)
        {
            digits[size] = carry % 10;
            carry /= 10;
            size++;
        }
    }

    int sum = 0;
    for (int i = 0; i < size; i++)
    {
        sum += digits[i];
    }

    printf("Sum of the digits of 100 factorial: %d\n", sum);

    return 0;
}
