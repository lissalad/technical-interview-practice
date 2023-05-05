# PROBLEM:
# Given an array a of n numbers and a count k find the k largest values in the array a.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]

# CLARIFYING:
# Can we assume that the length of a is greater than k?
# Should the output have 3 unique values? If there were another 7 in the list
# before the 6, would the output be [7, 8, 7]?
# Does it matter what order the returned list is in?
# If k=0, should we return an empty list?
# Might there be negative values in the array?
# Can I use the built in sort() method? min() or max()? (probably not)

# PSEUDOCODE:
# make new array equal to a
# while length of new array does not equal k
# remove minimum value
# return array

def largest_values(a, k):
    largest = a
    while len(largest) != k:
        largest.remove(min(largest))
    return largest


list = [5, 1, 3, 6, 8, 2, 4, 7]
print(largest_values(list, 3))

# FURTHER:
# Using the min() function lowers the efficiency of my solution.
# If I were to import heapq, I could manage finding the largest values
# by modifying the lists in place. This would improve the time complexity.
#
