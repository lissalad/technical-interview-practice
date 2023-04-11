# PROBLEM:
# Given an array a of n numbers and a count k find the k largest values in the array a.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]
#
# CLARIFYING:
# can I use sort()? array length less than k? negative input? does order of returned
#
#
# check if k is 0
# check if array a length is greater than k, or equal to
#

def greatest_in_array(a, k):
    if k == 0:
        return
    if k > len(a):
        return
    if k == len(a):
        return a

    a.sort(reverse=True)
    return a[:k]


print(greatest_in_array([5, 1, 3, 6, 8, 2, 4, 7], 3))
