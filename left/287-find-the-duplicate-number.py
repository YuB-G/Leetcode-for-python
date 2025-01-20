# Given an array of integers nums containing n + 1 integers 
# where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, 
# return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2

# slow = 1
# fast = 1

# slow = nums[1] = 3
# fast = num[nums[1]] = nums[3] = 2

# slow != fast
# slow = nums[3] = 2
# fast = nums[nums[2]] = nums[4] = 2'

# fast = 1
# slow = nums[2] = 4
# fast = nums[1] = 3

# slow = nums[4] = 2'
# fast = nums[3] = 2


def findDuplicate(self, nums: List[int]) -> int:
    slow = fast = nums[0]
    slow = nums[slow] 
    fast = nums[nums[fast]] 
    while slow != fast:
        slow = nums[slow] 
        fast = nums[nums[fast]] 

    # 第二阶段：寻找循环入口
    fast = nums[0] 
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast] 
    return slow