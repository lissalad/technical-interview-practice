# PROBLEM:
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# CLARIFYING:
# are the values in nums always of type int? (examples and leetcode function declaration suggest yes)
# must this be done in place? or can I make a new array?
# nums is not sorted?
# could there be leading zeros? like 1 and 01? are those unique?
# may I convert to a set? and convert to a list?

# PSEUDOCODE:
# create new array by converting nums to a set
# convert set back to array
# if new array equals nums, return False
# otherwise return True

def contains_duplicates(nums):
    unique_nums = set(nums)
    unique_nums = list(unique_nums)
    if nums == unique_nums:
        return False
    return True


print(contains_duplicates([1, 2, 3, 1]))
print(contains_duplicates([1, 2, 3, 4]))
print(contains_duplicates([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

# FURTHER:
# While this is not the least efficient, it is not the most efficient method either.
# Using a set avoided nested for loops, so that's good. Instead of checking that both lists
# are exactly equal, I could loop through nums and check if the value is in the set.
# As soon as a duplicate is found, it can exit the loop, rather than continue going
# through all the values.
