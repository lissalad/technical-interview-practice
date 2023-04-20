# PROBLEM:
# We are working on a scientific study we need a function that mixes up all of the letters in a word but,
# the first and last letter should be unchanged. For example: widget might become wgidet.

# CLARIFYING:
# what if the word is two letters or less? assuming we get a string? can we use random?
# could it possibly be returned the same?

# PSEUDOCODE:
# check length of word is greater than 2, if 3, return same word
# remove and store first letter and last in their own variables
# use random.shuffle() to scramble inner letters
# return the joined beginning and shuffled string and end

import random


def scrambled_inner_word(word):
    if len(word) < 4:
        return word

    start = word[0]
    end = word[-1]
    middle = ''.join(random.sample(word[1:-1], len(word)-2))

    return start + middle + end


print(scrambled_inner_word("widget"))
