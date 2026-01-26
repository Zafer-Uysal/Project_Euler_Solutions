// Project Euler – Problem 19
// Title: Counting Sundays
// Link: https://projecteuler.net/problem=19
//
// Count how many Sundays fell on the first day
// of the month during a given time period.

#include <stdio.h>

bool feb_is_leap(int year)
{
    return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
}

int main()
{
    int days_in_month[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int days_of_week = 0;
    int sundays = 0;

    for (int year = 1900; year < 2001; year++)
    {
        for (int month = 0; month < 12; month++)
        {
            if (year >= 1901 && days_of_week == 6)
            {
                sundays++;
            }
            
            int days = days_in_month[month];

            if (month == 1 && feb_is_leap(year))
            {
                days++;
            }
            
            days_of_week = (days_of_week + days) % 7;
        }
    }
    
    printf("Number of sundays fell on the first of the month during the twentieth century: %d", sundays);
    return 0;
}

