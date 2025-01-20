# Given an integer array nums of length n
# where all the integers of nums are in the range [1, n]
# and each integer appears once or twice, 
# return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time 
# and uses only constant extra space.

# Example:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]


# Thourght:
# 原地哈希
# 



# 4: nums[4-1] = nums[3] 变为 -7。
# [4, 3, 2, -7, 8, 2, 3, 1]

# 3：nums[3-1] = nums[2] 变为 -2。
# [4, 3, -2, -7, 8, 2, 3, 1]

# 2：nums[2-1] = nums[1] 变为 -3。
# [4, -3, -2, -7, 8, 2, 3, 1]

# 7：nums[7-1] = nums[6] 变为 -3。
# [4, -3, -2, -7, 8, 2, -3, 1]

# 8：nums[8-1] = nums[7] 变为 -1。
# [4, -3, -2, -7, 8, 2, -3, -1]

# 2：nums[2-1] = nums[1] 是负数，2是重复的。
# 添加 2 到结果

# 遇到数字 3：nums[3-1] = nums[2] 是负数，3是重复的。
# 添加 3 到结果


def findDuplicates(nums):
    duplicates = []
    for num in nums:
        # 获取数字对应的索引
        index = abs(num) - 1
        # 如果该位置的数字已经是负数，表示找到一个重复数字
        if nums[index] < 0:
            duplicates.append(abs(num))
        # 否则，将该位置的数字变为负数，表示该数字已经出现过一次
        else:
            nums[index] = -nums[index]
    return duplicates
