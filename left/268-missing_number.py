# Question:
# Given an array nums containing n distinct numbers 
# in the range [0, n], 
# return the only number in the range 
# that is missing from the array.

# Example:
# Input: nums = [3,0,1]
# Output: 2

# Input: nums = [0,1]
# Output: 2

# Thoughts/visualization:

# 1. Basic solution:

# [3,0,1]
# sort: [0,1,3]
# creative a index to numbers in range [0,n]

# first case: the missing number between range [0,n]
# if index != nums[i]
# index = 2  !=  nums[2] which is 3
# return index

# seconde case: the missing number is n
# After traversing all the numbers and no missing number is found, 
# then the last number n is the missing number.

class Number:
    def missingNumber(self, nums):
        nums.sort()
        length = len(nums)
        for i in range(length):
            if i != nums[i]:
                return i
        return length
    

# 2.Optimal solution:

# Using sum of range(0,n) minus original nums[]

# first case: the missing number in middle of nums
# [3,0,1]
# Sum of number in (0,n) minus sum of orignal nums [3,0,1]
# sum of (0,4) = 6 minus 4
# Equal 2

# Second case: the missing number is last number n
# [0,1,2]
# Sum of number in (0,n) minus sum of orignal nums [0,1,2]
# sum of (0,4) = 6 minus 3
# Equal 3


class Number:
    def missingNumber(self, nums):
        return sum(range(len(nums) + 1)) - sum(nums)
