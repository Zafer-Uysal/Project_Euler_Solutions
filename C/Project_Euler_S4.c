// Project Euler – Problem 4
// Title: Largest Palindrome Product
// Link: https://projecteuler.net/problem=4
//
// Find the largest palindrome made from the product
// of two n-digit numbers.

#include <stdio.h>

int isPalindrome(int number)
{
    int reversed = 0, original = number;

    while (number > 0)
    {
        reversed = reversed * 10 + (number % 10);
        number /= 10;
    }

    return original == reversed;
}

int main()
{
    int maxPalindrome = 0;

    for (int i = 100; i <= 999; i++)
    {
        for (int j = 100; j <= 999; j++)
        {
            int product = i * j;

            if (product > maxPalindrome && isPalindrome(product))
            {
                maxPalindrome = product;
            }
        }
    }

    printf("Largest palindrome: %d\n", maxPalindrome);
    return 0;
}
