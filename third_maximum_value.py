# PROBLEM:
# Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.

# CLARIFYING:
# would [1, 2, 2] return 1? or is there no third maximum, and would 2 be returned? ...
# / what does it mean by distinct?
# would [3, 3, 3] return 3?
# would [3, 3] also return 3?
# might it be empty?
# can i convert to set? to list?
# can i use max()?
# can i use sort()?

# PSEUDOCODE:
# check for empty, return None
# if the length is 1, return the one value
# use a set to make all values unique, then convert back to list
# if length of set is 1, return the one value
# if length is 2, check if first is greater than second, return that, otherwise return second
# repeat twice: remove max value from set
# return max from remaining set

def third_maximum_value(nums):
    if len(nums) == 0:
        return None

    nums = list(set(nums))
    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        if nums[0] > nums[1]:
            return nums[0]
        return nums[1]

    nums.remove(max(nums))
    nums.remove(max(nums))

    return max(nums)


print(third_maximum_value([3, 2, 1]))
print(third_maximum_value([1, 2]))
print(third_maximum_value([2, 2, 3, 1]))

# FURTHER:
# Another way to solve this would be using a variation of the selection sort algorithm.
# This would loop though the numbers updating a first, second, and third variable initialized
# as negative infinity. This is simpler in appearance, but not neccessarily more efficient.
