# Given a string s, find the length of the longest substring
# without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Visualization

# end = 0:

# s[end] 'a'
# hashmap = {'a': 1}
# max_len = 1。

# end = 1:

# s[end] 'b'
# hashmap = {'a': 1, 'b': 1}
# max(1, 2) = 2。

# (end = 2):

# s[end] 'c'
# hashmap = {'a': 1, 'b': 1, 'c': 1}
# max(2, 3) = 3。

# end = 3:

# s[end] 是 'a'
# hashmap = {'a': 2, 'b': 1, 'c': 1}
# 不更新 max_len。
# hashmap = {'a': 1, 'b': 1, 'c': 1}。
# start = 1

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, hashmap = 0, {}

        start = 0
        for end in range(len(s)):

            hashmap[s[end]] = hashmap.get(s[end], 0) + 1
            if len(hashmap) == end - start + 1:
                max_len = max(max_len, end - start + 1)
    
            while end - start + 1 > len(hashmap):
                head = s[start]
                hashmap[head] -= 1
                if hashmap[head] == 0:
                    del hashmap[head]
                start += 1
    
        return max_len