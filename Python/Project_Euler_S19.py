# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

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

