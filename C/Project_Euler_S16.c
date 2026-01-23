// Project Euler – Problem 16
// Title: Power Digit Sum
// Link: https://projecteuler.net/problem=16
//
// Find the sum of the digits of a number
// raised to a given power.

#include <stdio.h>

int main()
{
    int digits[400] = {0};
    digits[0] = 1;

    for (int i = 0; i < 1000; i++) 
    {
        int carry = 0;
        for (int j = 0; j < 400; j++) 
        {
            int val = digits[j] * 2 + carry;
            digits[j] = val % 10;
            carry = val / 10;
        }
    }

    int started = 0;
    int result = 0;
    for (int i = 399; i >= 0; i--) 
    {
        if (digits[i] != 0) 
        {
            started = 1;
        }
        if (started) {
            result += digits[i];
        }
    }
    printf("Sum of the digits of 2^1000: %d", result);
    return 0;
}

