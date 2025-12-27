// The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
// The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 552 = 3025
// Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
// Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

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