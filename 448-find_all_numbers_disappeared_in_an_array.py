# Question
# Given an array nums of n integers 
# where nums[i] is in the range [1, n], 
# return an array of all the integers 
# in the range [1, n] that do not appear in nums.

# Example:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Input: nums = [1,1]
# Output: [2]

# Thoughts/visualization:

# Basic solution:

# Find the number that not in set(nums)

# [4,3,2,7,8,2,3,1]
# create a index to traversal all number in range [1,n]
# set(nums) [1, 2, 3, 4, 7, 8]
# if not in set(nums), append to result
# result [5,6]

class Number:
    def findDisappearedNumbers(self, nums):
        result = []
        length = len(nums)
        count = set(nums)
        for i in range(1,length+1):
            if i not in count:
                result.append(i)
        return result