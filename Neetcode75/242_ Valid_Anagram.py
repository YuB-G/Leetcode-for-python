# Given two strings s and t, 
# return true if t is an anagram of s, 
# and false otherwise.

# An Anagram is a word or phrase formed 
# by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: True
# Example 2:

# Input: s = "rat", t = "car"
# Output: False

# Input: s = "aabc", t = "abcc"
# Output: False

# Thoughts/visualization:

# s: "anagram"
# t: "nagaram"

# s count {a:3, n:1, g:1, r:1, m:1}

# if character in t are also in s count[char] -=1
# if not in s count 
# return False
# count {a:0, n:0, g:0, r:0, m:0}

# all value equal 0
# return True

class solution:
    def valid_anagram(s:str, t:str):
        if len(s) != len(t):
            return False
        
        count = {}

        for i in s:
            if i in count:
                count[i] +=1
            else:
                count[i] = 1
        
        for j in t:
            if j in count:
                count[i] -= 1
            else:
                return False
        
        for value in count.values():
            if value != 0:
                return False


        return True