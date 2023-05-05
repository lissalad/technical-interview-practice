# PROBLEM:
# You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have.
# Each character in stones is a type of stone you have.
# You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# CLARIFYING:
# Both inputs are strings correct? Each character in jewels
# is a separate jewel? Are any jewels more than one character?

# PSEUDOCODE:
# initialize a jewel counter
# loop through stones, check if equal to any jewels, add to counter if so
# return counter

def jewels_stones(jewels, stones):
    counter = 0
    for stone in stones:
        for jewel in jewels:
            if stone == jewel:
                counter += 1
    return counter


print(jewels_stones("aA", "aAAbbbb"))

# FURTHER:
# My solution is the brute force solution. The nested for loops make this
# not very efficient. To improve this, a set could be used instead.
# If jewels were made into a set, there would only need to be one for loop,
# and then an if statement to check if the stone is in the set.
