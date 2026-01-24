// Project Euler – Problem 17
// Title: Number Letter Counts
// Link: https://projecteuler.net/problem=17
//
// Count the number of letters needed
// to write numbers in words within a range.

#include <stdio.h>
#include <string.h>

const char *ones[] = {
    "", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen",
    "fifteen", "sixteen", "seventeen", "eighteen",
    "nineteen"
};

const char *tens[] = {
    "", "", "twenty", "thirty", "forty",
    "fifty", "sixty", "seventy", "eighty", "ninety"
};

void number_to_words(int n, char *result) {
    result[0] = '\0';

    if (n < 20) {
        strcat(result, ones[n]);
    }
    else if (n < 100) {
        strcat(result, tens[n / 10]);
        strcat(result, ones[n % 10]);
    }
    else if (n < 1000) {
        strcat(result, ones[n / 100]);
        strcat(result, "hundred");

        if (n % 100 != 0) {
            strcat(result, "and");
            char temp[50];
            number_to_words(n % 100, temp);
            strcat(result, temp);
        }
    }
    else if (n == 1000) {
        strcat(result, "onethousand");
    }
}

int main() {
    int total_letters = 0;
    char word[100];

    for (int i = 1; i <= 1000; i++) {
        number_to_words(i, word);
        total_letters += strlen(word);
    }

    printf("From 1 to 1000 inclusive were written out in words, number of letters would be used: %d\n",
           total_letters);

    return 0;
}
