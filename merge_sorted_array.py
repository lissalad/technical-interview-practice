# PROBLEM:
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function,
# but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n,
# where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# CLARIFYING:
# By non-decreasing, does this mean increasing?
# Can we assume nums1 will always have a length of m + n with the correct number of zeros?
# Instead of returning, is it ok if I print the result within the function to check my work?
# Can we use the built in sort function?

# PSEUDOCODE:
# loop through nums1, STARTING at length of nums2 - 1
# replace current index with corresponding nums2 value
# return sorted array

def merge_sorted_array(nums1, nums2):
    index = len(nums1) - len(nums2)

    for num in range(len(nums2)):
        nums1[index] = nums2[num]
        index += 1

    nums1.sort()
    print(nums1)


merge_sorted_array([1, 2, 3, 0, 0, 0], [2, 5, 6])
