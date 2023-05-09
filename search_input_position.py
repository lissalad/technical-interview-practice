# PROBLEM:
# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# CLARIFYING:
# distinct means they are all unique? no duplicate values?
# will the target value also be an integer?

# PSEUDOCODE:
# set index count to 0
# loop while current int in list is not greater than
# add 1 to index count
# return index count

def search_input_position(nums, target):
    index = 0
    while nums[index] < target:
        index += 1
    return index


print(search_input_position([1, 3, 5, 6], 5))
print(search_input_position([1, 3, 5, 6], 2))

# FURTHER:
# While simple and easy to read, this solution is not the most efficient.
# It does not have O(log n) runtime complexity.
# Using a binary search would allow for the input position to be found much
# more efficiently. With each repetition, half of the possible answers
# would be ruled out.
