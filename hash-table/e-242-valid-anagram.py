# Given two strings s and t, 
# return true if t is an anagram of s, 
# and false otherwise.

# An Anagram is a word or phrase formed 
# by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Thoughts/visualization:

# s: "anagram"
# t: "nagaram"

# s count {a:3, n:1, g:1, r:1, m:1}

# in s count[char] -=1
# not in s count 
# return False
# t count {a:0, n:0, g:0, r:0, m:0}

# all value equal 0
# return True

# 一些思考：
# 为什么在第二个for loop 中，发现位于t中的字符不在s时 return False后，
# 还要再检测一遍count中的值来看有没有剩余的字符？
# 答案：一个反例可以是 s = "aabc" 和 t = "abcc
# s有的字母，t都有，但是他们并不是Anagram，即所有字母都一样，只是打乱了顺序。
# 所以需要再通过count.values检查一遍，这样会发现c的值不为0

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count={}

        for i in s:
            if i in count:
                count[i] +=1
            else:
                count[i] = 1

        for j in t:
            if j in count:
                count[j] -= 1
            else:
                return False

        for value in count.values():
            if value != 0:
                return False
            
        return True

