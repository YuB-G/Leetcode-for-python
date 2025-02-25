# Question:
# Given an integer array nums,
# return Ture if any value appears at least twice in the array
# and return flase if every element is distinct

# Example:
# input: nums = [1,2,3,1]
# output: true, 1 appears twice

# input: nums = [1,2,3,4]
# output: False, all number are unique

# Methods:

# 1.brute force:
# Nested loop

# i -> 1
# j-> i+1
# if nums[i] == nums[j] return True
# After traversing all the numbers return False

class Array:
    def contains_dupliucate(self, nums):
        for i in range(len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True 
        return False


# 2. Hashtable
# Thoughts/visualization

#[1,2,3,1]
# loop:
# if i not in dict, Assigned a random value:
# 1 not in dict: {1:1}
# 2 not in dict: {1:1,2:1}
#.....continue

# if i in dict:
    # retrun True
# last 1 in dict: {1:1,2:1,3:1}

# After traversing all the numbers 
    # return False

class Array:
    def containsDuplicate(self, nums):
        num_dict = {}
        for i in nums:
            if i in num_dict:
                return True
            num_dict[i] = 1
        return False
        
#3. set

# Thoughts/visualization

# [1,2,3,1]
# len(nums) = 4
# len(set(nums)) = 3
# cause set() do not cotain duplicate item 

class Array:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))