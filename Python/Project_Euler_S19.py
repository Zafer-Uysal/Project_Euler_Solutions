# Project Euler – Problem 19
# Title: Counting Sundays
# Link: https://projecteuler.net/problem=19
#
# Count how many Sundays fell on the first day
# of the month during a given time period.

def feb_is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = 0 
sundays = 0

for year in range(1900, 2001):
    for month in range(12):
        if year >= 1901 and day_of_week == 6:
            sundays += 1

        days = days_in_month[month]
        if month == 1 and feb_is_leap(year):
            days += 1

        day_of_week = (day_of_week + days) % 7

print("Number of sundays fell on the first of the month during the twentieth century: ", sundays)

