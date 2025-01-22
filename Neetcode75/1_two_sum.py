# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# thought:
# [2, 7, 11, 15] target = 9 dic = {}
# {2:0}

#重点: 算差值，其实就是找“配套”数字


class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target-num],i] # 如果没有找到，将当前数字及其索引存入字典
            dic[num] = i
        return []
    
# 第一轮 (i = 0, num = 2):
# target - num = 9 - 2 = 7，7 不在字典中
# 将 2 和它的索引 0 存入字典：dic = {2: 0}
# 第二轮 (i = 1, num = 7):
# target - num = 9 - 7 = 2，2 在字典中
# 返回 [dic[2], i] = [0, 1]

