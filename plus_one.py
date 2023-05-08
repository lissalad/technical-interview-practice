# PROBLEM:
# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in
# left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# CLARIFYING:
# What do you mean by "leading zeros"? Does that mean 1 is 1, not 01? or no [0, 1]?
# if digits[i] is the "ith" digit, then does that mean the 0th digit is in the ones place?
# can I use the join() and list() methods?
# can I force int and string?

# PSEUDOCODE:
# force string on each digit
# join list of sting digits into one string
# force int
# add one
# force string
# list characters into array
# force int on each
# return array

def plus_one(digits):
    for i in range(len(digits)):
        digits[i] = str(digits[i])

    digits = int("".join(digits))
    digits += 1

    digits = list(str(digits))

    for i in range(len(digits)):
        digits[i] = int(digits[i])

    return digits


print(plus_one([4, 3, 2, 1]))
print(plus_one([9, 9, 9]))

# FURTHER:
# This is not most efficient way to solve this problem.
# With another stratedgy, I could avoid unneccessary looping or converting of types.
# First, I would add 1 to the last digit.
# If this value were then above 9, I change it to 0, and repeat the steps on the next digit. I would repeat
# this until a digit does not go above 9.
# Then I would return the list of digits.


# For some reason I thought that this would require recursion
# so I just went ahead and implemented the brute force method
# before fully thinking out the more efficient solution I
# describe at the end.
