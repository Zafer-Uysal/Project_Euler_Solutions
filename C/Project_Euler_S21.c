// Project Euler – Problem 21
// Title: Amicable Numbers
// Link: https://projecteuler.net/problem=21
//
// Find the sum of all amicable numbers
// under a given limit.

#include <stdio.h>

int sum_of_divs(int n) {
    int sum_divs = 0;

    for (int i = 1; i < n; i++) {
        if (n % i == 0) {
            sum_divs += i;
        }
    }
    return sum_divs;
}

int main() {
    int x = 0, y = 0, z = 0;
    int amicable_sum = 0;

    while (x < 10000) {
        x++;
        y = sum_of_divs(x);
        z = sum_of_divs(y);

        if (x == z && x != y) {
            amicable_sum += x;
        }
    }
    printf("Sum of all the amicable numbers under 10000: %d\n", amicable_sum);
    return 0;
}



