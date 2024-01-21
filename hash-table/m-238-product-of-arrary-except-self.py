# Given an integer array nums, 
# return an array answer such that answer[i] 
# is equal to the product of all the elements of nums except nums[i].

# Example:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Thoughts/visualization:

# 分别计算每个元素的左乘积和右乘积
# 左乘积是这个数左边所有数字相乘
# 右乘积是这个数右边所有数字相乘

# left: for loop traversal nums,
# and make sure that first number is one,
# because the left side of first number is none
# set 1 can keep itself
# next number = nums[i-1]*left[i-1]

# right: answer[i] = left[i] * right[i]

# [1,2,3,4]
# left = [0,0,0,0]
# right = [0,0,0,0]
# answer = [0,0,0,0]

# left [1,0,0,0]
# left[1] = nums[0] * left[0] = 1x1=1

# left [1,1,0,0]
# left[2] = nums[1] * left[1] = 1x2=2

# left [1,1,2,0]
# left[3] = nums[2] * left[2] = 2x3=6

# left [1,1,2,6]

# right = [0,0,0,1]             
# right[2] = right[3] * nums[3] = 1 * 4 = 4

# right = [0,0,4,1]  
# right[1] = right[2] * nums[2] = 4 * 3 = 12
# right = [0,12,4,1]  
# right[0] = right[1] * nums[1] = 12 * 2 = 24

# right = [24,12,4,1]  

def product_except_self(nums):
    n = len(nums)
    left, right, answer = [0]*n, [0]*n, [0]*n
    
    left[0] = 1
    for i in range(1, n):
        left[i] = nums[i - 1] * left[i - 1]
        
    right[n - 1] = 1
    for i in reversed(range(n - 1)):
        right[i] = nums[i + 1] * right[i + 1]
        
    for i in range(n):
        answer[i] = left[i] * right[i]
        
    return answer


