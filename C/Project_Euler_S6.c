// Project Euler – Problem 6
// Title: Sum Square Difference
// Link: https://projecteuler.net/problem=6
//
// Find the difference between the square of the sum
// and the sum of the squares of the first n natural numbers.

#include <stdio.h>

int main()
{
int result = 0;

int x = 0;
int y = 0;
for (int i = 0; i <= 100; i++)
{
    x = i*i;
    y = x + y;
} 

int a = 0;
for (int k = 0; k <= 100; k++)
{
    a = a + k;
}

int b = 0;
b = a*a;
result = b - y;

printf("Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum: %d", result);
}