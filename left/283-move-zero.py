# Given an integer array nums, 
# move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Thoughts/visualization:

# Two point Two traversal:
# 快指针fast的作用：负责遍历数组的每一个元素。
# 如果遇到非零元素，这个元素要被移到前面去。
# 慢指针slow的作用：始终指向第一个零元素或者已经处理完毕的非零元素序列的下一个位置。
# 任何时候slow指针的左边都是处理好的非零元素。


# [0,1,0,3,12]
# s=0, f=0, 0=0 continue [0,1,0,3,12]
# s=0, f=1, 1 != 0 nums[s] = nums[f] [1,1,0,3,12]
# s=1, f=2, 0=0 continue [1,1,0,3,12]
# s=1, f=3, 3!=0 nums[s] = nums[f] [1,3,0,3,12]
# s=2, f=4, 12!=0 nums[s] = nums[f] [1,3,12,3,12]
# s=3
# all element from slow to end change to 0
# [1,3,12,0,0]
class Number:
    def moveZeroes(self, nums):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] !=0:
                nums[slow] = nums[fast]
                slow+=1
        for i in range(slow,len(nums)):
            nums[i] = 0


# Two point one traversal:
# fast point respond for traversal element
# if fast point met non-zero number if nums[f] !=0
# transfer with 0, slow point always point to zero
# nums[s],nums[f] = nums[f],nums[s]
# so, the number is non-zero change to left side
# the number is zero change to right side


# [0,1,0,3,12]
# s=0, f=0, 0=0 continue [0,1,0,3,12]
# s=0, f=1, 1 != 0 nums[s],nums[f] = nums[f],nums[s] [1,0,0,3,12]
# s=1, f=2, 0=0 continue [1,0,0,3,12]
# s=1, f=3, 3!=0 nums[s],nums[f] = nums[f],nums[s] [1,3,0,0,12]
# s=2, f=4, 12!=0 nums[s] = nums[f] [1,3,12,0,0]
class Solution:
    def moveZeroes(self, nums):
        s = 0
        for f in range(len(nums)):
            if nums[f]!=0:
                nums[s],nums[f] = nums[f],nums[s]
                s += 1