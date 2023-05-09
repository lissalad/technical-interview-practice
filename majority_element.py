# PROBLEM:
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# CLARIFYING:
# is n an input?
# can I use sort()?
# does nums always contain integers? I will assume so.
# what would [1,1,2,2,3,3,3] return? is the kind of scenario without a majority
# that I do not need to consider in my solution?
# should I round n/2 ?

# PSEUDOCODE:
# keep half nums length in variable majority_count
# initialize empty dictionary
# loop through nums
# if current number not in dictionary, add it with value of 1
# if exists, add 1 to its value
# if its value > majority count, return num


def majority_element(nums):
    majority_count = len(nums)/2
    counts = {}

    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        if (counts[num] > majority_count):
            return num


print(majority_element([3, 2, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))

# FURTHER:
# The looping used in my solution causes it to inefficient. To maximize efficiency,
# we could loop through nums keeping count and ruling out non-majority elements.
