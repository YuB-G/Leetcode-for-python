# question:

# Given a string s, 
# reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', 
# and they can appear in both lower and upper cases, more than once.

# Example:
# Input: s = "hello"
# Output: "holle"

# thought:

# Two point
# [h,e,l,l,o]
# i = 0, j = len-1
# while i<j:
# e in dic
# o in dic
# reverse [h,o,l,l,e]
# l not in dic...

# after traversal, join together

def reverse(s):
    dic = "aeiou"
    i = 0
    j = len(s)-1
    s_list = list(s)

    while i < j:
        if s_list[i] in dic:
            if s_list[j] in dic:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i+=1
                
            j-=1
        else:
            i+=1

    return "".join(s_list)