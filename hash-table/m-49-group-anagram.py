# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Thought:

# strs = ["eat","tea","tan","ate","nat","bat"]

# sorted
# s_key: ["aet", "aet", "ant", "aet", "ant", "abt"]

# {aet: [eat, tea, ate], ant:[tan, nat],abt:[bat]}

# 难点：
# Time complexity
# 时间复杂度
# 假设平均字符串长度为 L，那么对单个字符串进行排序的时间复杂度通常是 O(LlogL)
# 假设我们有 N 个字符串。由于我们需要对每个字符串进行排序，这部分的总时间复杂度就是 N 乘以单个字符串排序的时间复杂度，即 O(N*LlogL)。

# Space complexity
# 在最坏的情况下（没有任何字谜，每个字符串都是唯一的），
# 哈希表将包含 N 个键值对，每个键是一个长度为 L 的字符串。
# 所以，哈希表的空间复杂度大约是 O(N*L)。

class Solution:
    def groupAnagrams(self, strs):
        table = {}
        for s in strs:
            s_key = "".join(sorted(s))
            if s_key not in table:
                table[s_key] = [s]
            else:
                table[s_key].append(s)
        return list(table.values())