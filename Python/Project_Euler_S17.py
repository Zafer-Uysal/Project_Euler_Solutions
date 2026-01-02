# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 inclusive were written out in words, how many letters would be used?
# Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 
# 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

ones = {
    0: "",
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
    14: "fourteen", 15: "fifteen", 16: "sixteen",
    17: "seventeen", 18: "eighteen", 19: "nineteen"
}

tens = {
    20: "twenty", 30: "thirty", 40: "forty",
    50: "fifty", 60: "sixty", 70: "seventy",
    80: "eighty", 90: "ninety"
}

def number_to_words(n):
    if n < 20:
        return ones[n]

    if n < 100:
        return tens[n // 10 * 10] + ones[n % 10]

    if n < 1000:
        if n % 100 == 0:
            return ones[n // 100] + "hundred"
        else:
            return ones[n // 100] + "hundredand" + number_to_words(n % 100)

    if n == 1000:
        return "onethousand"

total_letters = 0
for i in range(1, 1001):
    word = number_to_words(i)
    total_letters += len(word)

print("from 1 to 1000 inclusive were written out in words, number of letters would be used: ", total_letters)
