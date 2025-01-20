# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating (交替) order, 
# starting with word1. 
# If a string is longer than the other, 
# append the additional letters onto the end of the merged string.
# Return the merged string.


# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a b c
# word2:  p q r
# merged: a p b q c r

# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a b 
# word2:  p q r s
# merged: a p b q r s

# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a b c d
# word2:  p q 
# merged: a p b q c d

def merge_string(self, word1, word2):

    i = 0
    j = 0
    len1 = len(word1)
    len2 = len(word2)
    result = []

    while i < len1 or j < len2:
        if i < len1:
            result.append(word1[i])
            i = i+1

        if j < len2:
            result.append(word2[j])
            j = j+1
            
    return "".join(result)
