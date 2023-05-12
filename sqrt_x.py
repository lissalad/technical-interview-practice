# PROBLEM:
# Given a non-negative integer x,
# return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# CLARIFYING:
# so sqrt(9) would return 3?
# and sqrt(10) would also return 3?
# and sqrt(80) would return 8?
# can I use built in rounding functions? may i import math?
# can I use double multiplication signs?

# PSEUDOCODE:
# verify valid input of positive integer
# check if 1 or 0, return x
# divide x in half, start trying and looping from there
# round down each time and compare

import math


def sqrt(x):
    if(x < 0):
        return "NEGATIVE INPUT!"

    if(math.floor(x) != x):
        return("NON INTEGER INPUT!")

    if(x == 0):
        return 0

    if(x < 4):
        return 1

    if(x == 4):
        return 2

    root = math.floor((x / 2) - 1)
    while (math.floor(root * root) >= x):
        root -= 1

    return math.floor(root)


print(sqrt(-3))

print(sqrt(1))
print(sqrt(1.9))

print(sqrt(4))

print(sqrt(8))
print(sqrt(67))
print(sqrt(143))


# ------- FURTHER --------------- #
# This is the brute force method that requires cycling through each value below half
# until the square root is found. This method is not very efficient.
#
# Instead, I could use a binary search with recursion to find the value
# much more efficiently. Instead of substracting one with each repetition,
# I would compare the squared value of the middle point of my possible
# root values to x. From there I would split the possible values in half and
# repeat the search on either the upper or lower half, depending if the squared value
# was greater than or lesser than x. Instead of checking one value at a time,
# I would instead be ruling out half of the possibilities with each cycle.
# Recursion would allow me to repeat this process deeper into the halves
# until the square root is found.

# def happy_number(num):
#     sqr_sum = 0

#     while num > 9:
#         digit = num // 10
#         print(digit)
#         sqr_sum += digit * digit

#     if sqr_sum == 1:
#         return True

#     return False