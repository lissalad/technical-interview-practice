# INCOMPLETE !!!
# trying to cycle through once first
# ------------------------------------------ #

# PROBLEM:
# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer,
# replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# CLARIFYING:
# so the input will always be positive?
# it is possible that it will loop endlessly? or should I account for that?

# PSEUDOCODE:
# repeat until sum of square digits is a one digit number, or less than 10


def happy_number(num):
    sqr_sum = 0

    while not num == 0:
        digit = num % 10
        sqr_sum += digit*digit
        num //= 10
        print(sqr_sum)

    if sqr_sum == 1:
        return True

    return False


print(happy_number(100))

# get all digits:

# def happy_number(num):
# sqr_sum = 0
# while num > 9:
#     digit = num % 10
#     print(digit)
#     num //= 10

# return num
